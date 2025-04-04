import os
import base64
from dotenv import load_dotenv
import streamlit as st
import requests
import urllib.parse
import random
import time
from PIL import Image
import base64
from langchain_community.llms import Ollama
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Load environment variables from .env file
load_dotenv()
GIPHY_API_KEY = os.environ.get("GIPHY_API_KEY")
if GIPHY_API_KEY is None:
    st.error("GIPHY_API_KEY not found. Check your .env file.")

def get_gif_url(query):
    """
    Search Giphy for a GIF based on the provided query and return a random URL from the results.
    """
    encoded_query = urllib.parse.quote(query)
    url = (
        f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}"
        f"&q={encoded_query}&limit=10&offset=0&rating=g&lang=en"
    )
    try:
        response = requests.get(url)
        if response.status_code != 200:
            st.error(f"Giphy API request failed with status code {response.status_code}")
            return None
        data = response.json()
        if not data.get("data"):
            st.warning("No GIF found for this query.")
            return None
        # Randomly choose one of the results
        random_gif = random.choice(data["data"])
        return random_gif["images"]["downsized"]["url"]
    except Exception as e:
        st.error("An error occurred while fetching the GIF: " + str(e))
        return None

# Helper function to encode an image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Set page configuration for a wide layout
st.set_page_config(page_title="Dad-GPT", layout="wide")

# Cache the model
@st.cache_resource
def load_model():
    return OllamaLLM(model="llama3.2")

model = load_model()

# Define the prompt template
template = """
You are a seasoned dad-joke comedian.

Given the list of dad-jokes below, use them as inspiration to answer the user's question with a new, original, creative dad-joke. Even if user gives you the same prompt make sure to come up with a different joke.
Each joke you give should match the theme that user chose.

Dad-joke examples:
{jokes}

User question:
{question}

User theme:
{theme}

Respond only with a single, creative dad-joke.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Main UI
cols = st.columns([1, 2, 1])
with cols[1]:
    image_path = r"C:\Users\Vanuhi\Documents\v4nui\IH_individual_projects\chatbot\dad-gpt_icon.png"
    img_base64 = get_base64_image(image_path)
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{img_base64}" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("Enter your prompt and choose your favorite joke flavor!")

    with st.form(key='joke_form'):
        # First row: Input + Dropdown
        col_input, col_theme = st.columns([3, 2])
        with col_input:
            question = st.text_input("Prompt", placeholder="Why did the chicken...")
        with col_theme:
            theme = st.selectbox("Joke Theme", ["Classic Dad Jokes", "Puns", "One-Liners"])

        st.markdown(" ")
        # Second row: Centered Button using 3 columns
        col1, col2 = st.columns([3, 4])
        with col2:
            submitted = st.form_submit_button("Generate Dad Joke")

        if submitted:
            if question:
                jokes = retriever.invoke(question)
                result = chain.invoke({"jokes": jokes, "question": question, "theme": theme})
                st.markdown("### Here's Your Dad Joke!")
                st.success(result)
                
                # Retrieve a related GIF from Giphy
                gif_query = "funny dad joke"
                gif_url = get_gif_url(gif_query)
                if gif_url:
                    st.image(gif_url, caption="Here's a fun GIF for you!", use_container_width=True)
                else:
                    st.warning("No fun GIF found for this one!")
            else:
                st.error("Please enter a question before submitting.")

# Footer at the bottom center
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 12px;
    color: #888;
    padding: 5px 0;
}
</style>
<div class="footer">
    <p>Made with 💖 using Streamlit, LangChain, Ollama, and Giphy for endless dad jokes! Stay cheesy 🙃</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
