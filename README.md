## Building toward Computer Use with Anthropic  

---

This repository contains a set of practical updated and personalized notebooks based on the [Building Toward Computer Use with Anthropic short course](https://www.deeplearning.ai/courses/building-toward-computer-use-with-anthropic), created by [DeepLearning.AI](https://www.deeplearning.ai/courses) in collaboration with [Anthropic](https://platform.claude.com/docs).   

The [Building Toward Computer Use with Anthropic](https://www.deeplearning.ai/courses/building-toward-computer-use-with-anthropic) covers concepts of Anthropic in a progressive order: `API interaction`, `multimodal understanding`, `structured prompting`, and `tool use`. This repository follows that path and builds toward an agent-style workflow that can complete real tasks with the help of tools.

---  
### Why Anthropic?

[Anthropic](https://www.anthropic.com/)  emphasizes research-driven AI development, with a focus on multimodal understanding, prompt design, and tool-augmented systems. Claude's API offers a practical environment to experiment with these ideas and apply them in real-world workflows.

---  

## Repository Contents 

The repository is organized into four notebooks, each focused on a different concept from the practical learning path.  

| Module | Topics |
| --- | --- |
| **[Working with the API](./Working_with_API.ipynb)** | Simple text requests, message format, model parameters |
| **[Multimodal Requests & Streaming](./Multimodal_Requests_Streaming.ipynb)** | Single-image requests, multi-image + text requests, streaming  |
| **[Real World Prompting](./Real_World_Prompting.ipynb)** | Prompting chatbots vs. scalable prompt templates, practical prompting strategies |
| **[Tool Use](./Tool_Use_Streamlit.ipynb)** | Tool use overview, end-to-end tool-use flow |

---
## Repository Structure  

The project root contains the main notebooks, utility scripts, example assets, and environment configuration files.

```
DeepLearningAI_Anthropic-main/
├── images/
│   ├── food.png
│   ├── invoice.png
│   ├── packages.png
│   └── plant.png
├── requirements.txt
├── .env_example
├── helper.py
├── Working_with_API.ipynb
├── Multimodal_Requests_Streaming.ipynb
├── Real_World_Prompting.ipynb
├── Tool_Use_Streamlit.ipynb
├── app.py
├── support_backend.py
├── Screenshot_Tool_Use_Streamlit.jpeg
├── README.md
├── LICENSE
````
---

## What you'll find 

- **Hands-on notebooks** covering Anthropic API usage, multimodal inputs, structured prompting, streaming, prompt caching, and tool calling.  
- **Practical examples** that connect Claude's capabilities to real-world AI application patterns.  
- **A Progressive learning path** from basic API interaction to more advanced, tool-augmented workflows.   
- **Practice exercises** designed to reinforce the concepts introduced in each notebook.  

The overall goal is to move beyond simple conversational interactions and explore how models, tools, context, and execution loops can be combined to build more capable AI applications.    

 ---
 
## Getting started  

### Prerequisites   
- Python 3.10+  
- Google Colab or Jupyter environment  
- An Anthropic API key 

### Clone and install    

```bash
git clone https://github.com/micag2025/DeepLearningAI_Anthropic.git
cd DeepLearningAI_Anthropic
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt  
```

### Configure environment variables  

Copy the example environment file, `.env.example` and add your API key:  

```bash  
cp .env.example .env
```

Then update .env with your Anthropic API key and any required settings.  

---

## Contributions  

Contributions are welcome! If you would like to improve the examples, fix issues, or add new projects and notebooks, feel free to submit a [pull request](https://github.com/micag2025/DeepLearningAI_Anthropic/pulls). Community feedback and additional examples are encouraged.

---

## Resources  

- [Claude Platform Docs](https://platform.claude.com/docs)
- [Deelplearning.AI](https://www.deeplearning.ai/courses)
- [Anthropic](https://www.anthropic.com/)   

---

## Licence  

This repository is licensed under the [MIT License](
https://github.com/micag2025/DeepLearningAI_Anthropic/blob/141309985cf2e9dbfc8c1e27702acf2796e272e1/LICENSE).

