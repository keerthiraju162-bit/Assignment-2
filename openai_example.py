import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def query_openai(prompt):
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

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying OpenAI...")
    result = query_openai(user_prompt)
    print("Response:")
    print(result)
