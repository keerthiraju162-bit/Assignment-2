import os
import openai
import groq
import requests
import google.generativeai as genai
import cohere

def query_openai(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def query_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    client = groq.Groq(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def query_ollama(prompt):
    try:
        payload = {"model": "llama3", "prompt": prompt, "stream": False}
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        return response.json().get("response", "No response received.")
    except Exception as e:
        return f"Error: {str(e)}"

def query_huggingface(prompt):
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 500}}
        response = requests.post(MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return data[0].get("generated_text", "No response received.")
        return str(data)
    except Exception as e:
        return f"Error: {str(e)}"

def query_gemini(prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(max_output_tokens=500, temperature=0.7)
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def query_cohere(prompt):
    api_key = os.getenv("COHERE_API_KEY")
    co = cohere.Client(api_key)
    try:
        response = co.generate(model="command", prompt=prompt, max_tokens=500, temperature=0.7)
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

PROVIDERS = {
    "1": ("OpenAI (GPT-3.5)", query_openai),
    "2": ("Groq (Llama3)", query_groq),
    "3": ("Ollama (Local)", query_ollama),
    "4": ("Hugging Face (Mistral)", query_huggingface),
    "5": ("Google Gemini", query_gemini),
    "6": ("Cohere (Command)", query_cohere),
}

if __name__ == "__main__":
    print("=== Multi-API Query Tool ===")
    print("Select an AI provider:")
    for key, (name, _) in PROVIDERS.items():
        print(f"  {key}. {name}")

    choice = input("Enter your choice (1-6): ").strip()
    if choice not in PROVIDERS:
        print("Invalid choice. Exiting.")
    else:
        provider_name, query_fn = PROVIDERS[choice]
        user_prompt = input("Enter your prompt: ")
        print(f"Querying {provider_name}...")
        result = query_fn(user_prompt)
        print("Response:")
        print(result)
