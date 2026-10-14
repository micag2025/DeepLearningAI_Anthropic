## Building toward Computer Use with Anthropic  

---

This repository contains updated and personalized notebooks based on the learning material from the [Building Toward Computer Use with Anthropic short course](https://www.deeplearning.ai/courses/building-toward-computer-use-with-anthropic), created by [DeepLearning.AI](https://www.deeplearning.ai/courses) in collaboration with [Anthropic](https://platform.claude.com/docs).   

The learning path of the [Building Toward Computer Use with Anthropic](https://www.deeplearning.ai/courses/building-toward-computer-use-with-anthropic) introduces a powerful capability from Anthropic, focusing on how Claude can reason about `visual inputs`, `use tools`, and `work with multimodal context` to act more like an AI assistant than a static chatbot.

To explore Anthropic's approach to AI research, safety, alignment, and interpretability, this repository walks through the core concepts covered in the learning path using the Anthropic API. The notebooks cover API fundamentals, multimodal prompting, streaming responses, prompt caching, and tool use.

Each topic builds toward a final demonstration in which an agent combines these capabilities to perform practical tasks within a real-world workflow.

---  
### Why Anthropic?

Anthropic stands out for its practical, research-driven approach to building capable AI systems that combine multimodal understanding, structured prompting, and tool use. Through Claude’s API, the users can move beyond simple chat interactions and explore how models can be integrated into real workflows for reasoning, execution, and agent-like behavior.

---  

## Repository Contents 

The repository is organized into four notebooks, each focusing on a key concept introduced in the course. The notebooks progressively move from basic API interaction to multimodal applications and tool-augmented workflows.

| Notebook | Topics |
|---|---|
| **Working with the API** | API setup, authentication, messages, model parameters |
| **Multimodal Requests & Streaming** | Images, multimodal prompts, streaming |
| **Real-World Prompting** | XML prompts, examples, prompt caching |
| **Tool Use** | Tool calling, multi-tool workflows, agents |

---

## What's inside    

- **Hands-on notebooks** covering Anthropic API usage, multimodal inputs, structured prompting, streaming, prompt caching, and tool calling with Claude.  
- **Practical examples** connecting Claude's capabilities with real-world AI application patterns.
- **Progressive learning** that moves from basic API interaction and prompt engineering toward tool-augmented and agent-like workflows.    
- **Practice exercises** designed to reinforce the concepts introduced in each notebook.

The repository is designed to be approachable and practical, whether you are learning the basics of API interaction or experimenting with tool-using AI assistants.

The overall goal is to move beyond simple conversational interactions and explore how models, tools, context, and execution loops can be combined to build more capable AI applications.

 ---
 
## Getting started  

This section shows how to install dependencies, configure authentication, and run the full pipeline.

_Prerequisites:_    
- Python 3.10+  
- Google Colab or Jupyter environment  
- Anthropic API key (see .env_example)  

_Clone and install_  

```bash
git clone https://github.com/micag2025/DeepLearningAI_Anthropic.git
cd DeepLearningAI_Anthropic
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
Configure environment variables (see .env.example)
```

---

## Contributions  

Contributions are welcome! If you would like to improve the examples, fix issues, or add new projects and notebooks, feel free to submit a [pull request](https://github.com/micag2025/DeepLearningAI_Anthropic/pulls). Community feedback and additional examples are encouraged.

---

## Resources  

- [Claude Platform Docs](https://platform.claude.com/docs)
- [Deelplearning.AI](https://www.deeplearning.ai/courses)  

---

## Licence  

This repository is licensed under the [MIT License](
https://github.com/micag2025/DeepLearningAI_Anthropic/blob/141309985cf2e9dbfc8c1e27702acf2796e272e1/LICENSE).

