from openai import OpenAI
client = OpenAI() 

user_prompt = input("Enter your prompt: ")
system_prompt = "You are a helpful assistant that provides concise and accurate answers to user queries."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print("Response from OpenAI:")
print(response.choices[0].message.content)