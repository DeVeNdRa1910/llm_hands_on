from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from config import ENV_CONFIG

model = init_chat_model(f"groq:{ENV_CONFIG.LLM_MODEL}")

def create_story_chain():
    # Template for story generation
    story_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a great creative and thriller storyteller. Write a short and engaging story based on a given theme, character and setting."),
        ("user", "Theme: {theme}\n Main character: {character}\n Setting: {setting}")
    ])

    # Template for story analysis
    analysis_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are literally a critic. Analyze the following story and provide insights."),
        ("user", "{story}")
    ])

    story_chain = (
        story_prompt | model | StrOutputParser()
    )

    # creating a function to pass the story to analysis
    def analyze_story(story_text):
        return {"story": story_text}

    analysis_chain = (
        story_chain
        | RunnableLambda(analyze_story)
        | analysis_prompt 
        | model 
        | StrOutputParser()
    )

    # StrOutputParser() -> convert AIMessage output in to string formate

    return analysis_chain

chain = create_story_chain()

response = chain.invoke({
    "theme": "Crime Thriller",
    "character": "a prostitute girl",
    "setting": "new girl for prostitution"

})
print(response)