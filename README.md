# AI API Integration

A Python project that integrates six different Generative AI providers: OpenAI, Groq, Ollama, Hugging Face, Google Gemini, and Cohere.

## Project Structure

```
Assignment 2/
├── openai_example.py
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── multi_api_query.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Obtain API Keys

| Provider | URL |
|---|---|
| OpenAI | https://platform.openai.com/api-keys |
| Groq | https://console.groq.com/ |
| Ollama | https://ollama.ai/ (local install, no key needed) |
| Hugging Face | https://huggingface.co/settings/tokens |
| Google Gemini | https://makersuite.google.com/app/apikey |
| Cohere | https://dashboard.cohere.com/ |

### 3. Set Environment Variables

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-openai-key"
$env:GROQ_API_KEY="your-groq-key"
$env:HUGGINGFACE_API_KEY="your-hf-key"
$env:GOOGLE_API_KEY="your-google-key"
$env:COHERE_API_KEY="your-cohere-key"
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your-openai-key"
export GROQ_API_KEY="your-groq-key"
export HUGGINGFACE_API_KEY="your-hf-key"
export GOOGLE_API_KEY="your-google-key"
export COHERE_API_KEY="your-cohere-key"
```

### 4. Ollama Setup

Download and install from https://ollama.ai/, then pull a model:
```bash
ollama pull llama3
```

## How to Run Each Program

```bash
python openai_example.py
python groq_example.py
python ollama_example.py
python huggingface_example.py
python gemini_example.py
python cohere_example.py

# Bonus: Multi-provider tool
python multi_api_query.py
```

## Screenshots

Screenshots of each program's output are in the `screenshots/` folder.
