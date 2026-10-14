import streamlit as st

from support_backend import client, MODEL_NAME, tools, process_tool_call

st.set_page_config(page_title="Acme Co Support", page_icon="💬")
st.title("Acme Co Customer Support")
st.caption("Ask about customers, orders, or order cancellations.")

SYSTEM_PROMPT = """You are a helpful customer-support assistant for Acme Co, an online retailer.
Help users look up customers and orders and cancel eligible orders.
Use the available tools when needed. If required information is missing, ask a follow-up question.
Never invent customer or order information. Keep responses clear and concise.
"""


def run_assistant(messages):
    """Run Claude and execute requested tools until Claude finishes."""
    while True:
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            text_blocks = [
                block.text for block in response.content
                if getattr(block, "type", None) == "text"
            ]
            return "\n\n".join(text_blocks) or "No text response was generated."

        if response.stop_reason != "tool_use":
            raise RuntimeError(f"Unexpected stop reason: {response.stop_reason}")

        tool_results = []
        for block in response.content:
            if getattr(block, "type", None) != "tool_use":
                continue
            try:
                result = process_tool_call(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                })
            except Exception as exc:
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": f"Tool execution failed: {exc}",
                    "is_error": True,
                })

        if not tool_results:
            raise RuntimeError("Claude requested tool use but no tool calls were found.")
        messages.append({"role": "user", "content": tool_results})


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "api_messages" not in st.session_state:
    st.session_state.api_messages = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you?"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.session_state.api_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Checking your request..."):
            try:
                reply = run_assistant(st.session_state.api_messages)
                st.markdown(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
            except Exception as exc:
                st.error(f"Something went wrong: {exc}")
