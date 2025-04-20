# Multimodal AI Research Assistant

## 📌 Overview

This project implements a **Multimodal AI Research Assistant** capable of understanding and processing multimodal inputs—text, images, and audio. It retrieves relevant information, generates insightful responses, and maintains contextual memory over long interactions.

### ✨ Core Features
- **Agentic AI Framework**: Specialized agents for tasks like retrieval, summarization, and generation collaborate for complex goals.
- **LLMs with RAG**: Retrieval-Augmented Generation using GPT-4 or Claude ensures up-to-date, accurate responses.
- **Computer Vision (VLM)**: Vision-Language Models (e.g., BLIP-2) to understand and answer questions about images.
- **Diffusion Models**: Generate images from text prompts using Stable Diffusion.
- **Memory-Augmented Control (MCP)**: Retains memory of previous interactions and user preferences.

---

## 🧠 Technologies Used

- **LangChain / LlamaIndex** – Agent management + RAG
- **OpenAI GPT-4 / Claude** – Large Language Models
- **BLIP-2** – Vision-language model for image understanding
- **Stable Diffusion** – Text-to-image generation
- **Python, PyTorch, Transformers**
- **Docker** – For scalable deployment
- **NVIDIA Jetson Orin** – Edge deployment

---

## 📁 Project Structure

multimodal_ai_assistant/
│
├── agents/                    # Agent modules (future use)
├── core/                      # Core logic and memory
│   ├── controller.py          # Central controller for managing agents
│   ├── memory.py              # Memory management for past interactions
├── models/                    # Model wrappers for LLM, Vision, Diffusion
│   ├── llm_rag.py             # LLM with Retrieval-Augmented Generation
│   ├── vlm_blip.py            # Vision-Language Model integration (BLIP)
│   ├── diffusion_gen.py       # Diffusion model for image generation
├── data/                      # For any external datasets or files
├── main.py                    # Entry point for the assistant
├── requirements.txt           # List of required Python libraries
├── Dockerfile                 # Optional Docker container setup
└── .env                       # Store your API key (OpenAI)


## Install Dependencies

pip install -r requirements.txt


## 🔑 Configuration

OPENAI_API_KEY=your-openai-key-here


##  Running the Project . . . 

In the PyCharm terminal or command line, activate your virtual environment and run:
python main.py

You will see:
[Mode: text / image / generate / exit]:


## 📄 License
This project is licensed under the MIT License.


