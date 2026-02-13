from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from config import ENV_CONFIG

model = init_chat_model(f"groq:{ENV_CONFIG.LLM_MODEL}")


# for example we are creating the translation app

translation_template = ChatPromptTemplate.from_messages([
    ("system", "You are a professional translator. Translate the follow text {text} from {source_language} to {target_language}. Maintain the tone and behaviour style."),
    ("user", "{text}")
])

prompt = translation_template.invoke({
    "source_language": "English",
    "target_language": "Hinglish",
    "text": "LangChain is a powerful framework designed to help developers build applications powered by large language models. It provides tools for chaining together prompts, models, and external data sources to create more intelligent and context-aware systems. With LangChain, you can connect LLMs to databases, APIs, and documents to build chatbots, question-answering systems, and automation workflows. It supports memory management, allowing applications to maintain conversation history and context over time. Overall, LangChain simplifies the process of turning raw language models into practical, production-ready AI applications.",
})

translated_response = model.invoke(prompt)

print(translated_response.content)