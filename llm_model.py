from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from config import ENV_CONFIG

model = init_chat_model(f"groq:{ENV_CONFIG.LLM_MODEL}")

# print(model)

print("----------------------------------------------------------------------------------------------------------------------------------")

# we have one more another way to initialise the model but that is old way
# from langchain_groq import ChatGroq
# llm = ChatGroq(model=ENV_CONFIG.LLM_MODEL)
# print(llm)

messages = [
    SystemMessage("You are a helpful AI assistant"),
    HumanMessage("What are the top 3 benefits of using langchain?")
]

# now we have to invoke the model

response=model.invoke(messages)

print(response)
print("----------------------------------------------------------------------------------------------------------------------------------")
print(response.content)

# Also we can print the model by chunk

for chunk in model.stream(messages):
    print(chunk.content, end="", flush=True)