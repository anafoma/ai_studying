import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model = "gpt-4.1-nano",
    input = [
    {"role":"system", "content":"You are a senior backend engineer"},
    {"role":"user", "content":"Write a python function that adds two numbers"}
    ],
    temperature = 0.2
)

print(response.output[0].content[0].text)