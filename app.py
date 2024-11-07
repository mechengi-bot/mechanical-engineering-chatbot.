import streamlit as st
import openai
from googletrans import Translator

# Set up OpenAI API key (replace 'your_openai_api_key' with your actual API key)
openai.api_key = "sk-...ZHMA"

# Initialize the translator
translator = Translator()

# Define supported languages
languages = {
    "English": "en",
    "Arabic": "ar",
    "French": "fr"
}

# Configure the Streamlit page
st.set_page_config(page_title="Mechanical Engineering Chatbot", page_icon=":robot:", layout="centered")

# Set up chatbot appearance with purple and blue theme
st.markdown(
    """
    <style>
    .main {
        background-color: #F5F5F5;
    }
    .stButton > button {
        color: white;
        background-color: #6a0dad;
        border-color: #4c00c2;
    }
    .stTextInput > div > div > input {
        color: #4c00c2;
    }
    .stMarkdown {
        color: #6a0dad;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the header
st.title("🤖 Mechanical Engineering Chatbot")
st.write("Ask me about anything related to Mechanical Engineering! 🌍")

# Language selection
selected_language = st.selectbox("Choose your language / Choisissez votre langue / اختر لغتك", options=list(languages.keys()))

# Function to generate chatbot response
def generate_response(user_input, language):
    # Translate user input to English
    if language != "en":
        user_input = translator.translate(user_input, dest="en").text

    # Define prompt
    prompt = (
        "You are a chatbot specialized in answering questions about mechanical engineering, including "
        "career prospects, lessons, job opportunities, admission requirements, sectors that require mechanical engineers, "
        "and the relation of mechanical engineering with FST Tanger. Respond to each question based on this context."
        f"\nUser: {user_input}\nChatbot:"
    )

    # Generate response from OpenAI's GPT-4
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.6
    ).choices[0].text.strip()

    # Translate response back to the selected language if necessary
    if language != "en":
        response = translator.translate(response, dest=language).text
    return response

# User input
user_input = st.text_input("Type your question here")

# Handle submit
if st.button("Ask"):
    if user_input:
        language_code = languages[selected_language]
        response = generate_response(user_input, language_code)
        
        # Display the response
        st.write(response)
    else:
        st.write("Please enter a question.")
