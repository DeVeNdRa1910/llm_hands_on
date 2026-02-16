from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# streamlit is for frontend only

# page config
st.set_page_config(page_title="Simple LangChain Chatbot with groq", page_icon="⚔️")

# Title
st.title("Simple langchain chat with groq")
st.markdown("Learn langchain basics with groq's ultra-fast interference!")

with st.sidebar:
    st.header("Settings")

    # API key
    api_key = st.text_input("GROQ API key", type="password", help="Get Free API key from ")
    
    # Model selection
    model_name = st.selectbox(
        "Model",
        ["llama-3.1-8b-instant", "gemma2-9b-it"],
        index=0
    )

    # clear button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize the LLM
@st.cache_resource
def get_chain(api_key, model_name):

    if not api_key:
        return None
    
    # Initialize the groq model
    llm = ChatGroq(groq_api_key=api_key, model_name=model_name, temperature=0.7, streaming=True)

    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are helpful assistant powered by Grok. Answer question clearly and consisely."),
        ("user", "{question}")
    ])

    # Now we are creating chain
    return prompt | llm | StrOutputParser


# get chain
chain = get_chain(api_key, model_name)

if not chain:
    st.warning("Please enter your groq api key in the sidebar to start chatting!")
    st.markdown("[Get your free API key here](https://console.groq.com)")

else: 
    # Display the chat messge
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    #Take the input from the chat
    if question:=st.chat_input("Ask me anything"):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            #Stream response from groq
            for chunk in chain.stream({"question": question}):
                full_response += chunk
                message_placeholder.markdown(full_response+" ")
            message_placeholder.markdown(full_response)

            # Add to hostory
            st.session_state.messages.append({"role": "assistent", "content": full_response})
            
        except Exception as e:
            st.error(f"Error: {str(e)}")