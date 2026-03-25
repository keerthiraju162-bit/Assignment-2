import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt, model="llama3"):
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No response received.")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Ollama (local)...")
    result = query_ollama(user_prompt)
    print("Response:")
    print(result)
