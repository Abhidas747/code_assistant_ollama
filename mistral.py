import streamlit as st
from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="mistral")


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
st.title("Ollama Chatbot - mistral")

with st.expander("About"):
    st.write("A chat interface for the Ollama model.")

st.write("Enter your prompt below and get a response from the Ollama model.")

# Create adjustable text input field
prompt_area = st.text_area("Prompt:", height=10, key="prompt")
response = ""  # Initialize an empty string for the response variable

if st.button("Get Response"):
    if prompt_area.strip():
        response = generate_ollama_response(prompt_area)
        st.markdown("### Response from Ollama:")
        st.write(response)

# Update the response as user types
if prompt_area != st.session_state["prompt"]:  # Compare the current and previous values of the text area
    if prompt_area.strip():
        response = generate_ollama_response(prompt_area)
        st.markdown("### Response from Ollama:")
        st.write(response)
    st.session_state["prompt"] = prompt_area  # Update the session state with the new value of the text area
