import cohere
import os

api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

def query_cohere(prompt):
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Cohere...")
    result = query_cohere(user_prompt)
    print("Response:")
    print(result)
