import requests
import os

api_key = os.getenv("HUGGINGFACE_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

def query_huggingface(prompt):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 500}}
        response = requests.post(MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("generated_text", "No response received.")
        return str(data)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Hugging Face...")
    result = query_huggingface(user_prompt)
    print("Response:")
    print(result)
