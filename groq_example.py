import groq
import os

api_key = os.getenv("GROQ_API_KEY")
client = groq.Groq(api_key=api_key)

def query_groq(prompt):
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

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Groq...")
    result = query_groq(user_prompt)
    print("Response:")
    print(result)
