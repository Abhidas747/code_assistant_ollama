import streamlit as st
from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="codegemma")


# Function to generate response using Ollama
def generate_ollama_response(prompt):
    response = llm.invoke(prompt)

    # Handle cases where response is not structured as expected
    if isinstance(response, str):
        return response  # Return the string response directly

    # Handle cases where response is structured
    if 'output' in response and response['output']:
        return response['output'][0].get('text', 'No response found')
    else:
        return 'No response found'


# Streamlit app
st.title("Ollama Chatbot - codegemma")
st.write("Enter your prompt below and get a response from the Ollama model.")

prompt = st.text_input("Prompt:")

if st.button("Get Response"):
    if prompt.strip():
        response = generate_ollama_response(prompt)
        st.markdown("### Response from Ollama:")
        st.write(response)
    else:
        st.write("Please enter a prompt.")