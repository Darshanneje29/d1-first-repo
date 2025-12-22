from langchain_groq import ChatGroq
import os

api_key=os.getenv("groq_api")
llm=ChatGroq(model="openai/gpt-oss-120b", api_key=api_key)


user_input = input("You: ")

result = llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")