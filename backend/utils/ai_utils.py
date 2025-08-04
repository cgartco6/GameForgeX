import openai  # We'll use OpenAI API as an example

# Set your OpenAI API key (use environment variable in production)
openai.api_key = "your-api-key"

def generate_with_ai(prompt, model="gpt-3.5-turbo", max_tokens=1500):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that generates code and solutions for technical tasks."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
