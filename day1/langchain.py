import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")

llm = ChatOpenAI(model="gpt-4.1-nano", temperature = 0.2, api_key = OPENAI_API_KEY)

input = [
    {"role":"system", "content":"You are a senior backend engineer"},
    {"role":"user", "content":"Write a python function that adds two numbers"}
]

response = llm.invoke(input)

print(response)
print(response.content)