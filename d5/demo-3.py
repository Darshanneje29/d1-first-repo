from langchain.chat_models import init_chat_model
import os

llm=init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("groq_api")
)

connversation=list()
while True:
    user_input=input("You: ")
    if user_input=="exist":
        break
    user_msg={"role":"user","content":user_input}
    connversation.append(user_msg)
    llm_output=llm.invoke(connversation)
    print("AI:", llm_output.content)
    llm_msg={"role":"assistant","content":llm_output.content}
    connversation.append(llm_msg)