<p align="left">
  <img src="dad-gpt_icon.png" alt="Dad-GPT Logo" width="150"/>
</p>

A Streamlit-based web app that generates creative dad jokes using a local language model (Ollama) integrated via LangChain. The app also enhances the experience by fetching a related GIF from Giphy. Additionally, the project includes scripts to collect dad jokes from Reddit using PRAW and perform exploratory data analysis (EDA) to prepare the data for a Retrieval-Augmented Generation (RAG) pipeline.

## Features

- 🤓 **Generative Dad Jokes:**  
  Uses a fine-tuned local language model to generate creative and unique dad jokes.

- 🎞️ **Dynamic GIF Integration:**  
  Retrieves a related GIF from Giphy based on the generated joke context.

- 👨‍💻 **Reddit Data Collection:**  
  Utilizes PRAW (Python Reddit API Wrapper) to collect dad jokes from the [dadjokes subreddit](https://www.reddit.com/r/dadjokes/).

- 📊 **Data Preparation & EDA for RAG:**  
  Performs exploratory data analysis (EDA) on the collected jokes to clean, analyze, and format the data for use in a Retrieval-Augmented Generation (RAG) system.

## 🧰 Prerequisites

- 🐍 **Python Version:** Python 3.8 – 3.11 (Python 3.12 may cause compatibility issues with some dependencies)
- 📦 **Virtual Environment:** Recommended for dependency management
- 🔑 **API Keys:**
  - Giphy API Key ([Get one here](https://developers.giphy.com/))
  - Reddit API credentials (for PRAW; [Learn how to obtain them](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html))

## ⚙️ Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create and Activate a Virtual Environment:**

   ```
   python -m venv chatbot-venv
   # On Windows:
   chatbot-venv\Scripts\activate
   # On macOS/Linux:
   source chatbot-venv/bin/activate
   ```

3. **Install Dependencies:**
   Install them with:
   ```
   pip install -r requirements.txt
   ```

4 **Configure Environment Variables:**
Create a .env file in the project root with your API credentials:

```
GIPHY_API_KEY=your_giphy_api_key_here
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
REDDIT_USER_AGENT=your_reddit_user_agent_here
```

## 🚀 Usage

### 1. 🧠 Collecting Dad Jokes from Reddit

Use the provided script (`collect_dadjokes.py`) to fetch dad jokes from the [dadjokes subreddit](https://www.reddit.com/r/dadjokes/) using PRAW.

```bash
python collect_dadjokes.py
```

This script will:

- Connect to Reddit using your API credentials.
- Fetch dad jokes from the subreddit.
- Save the jokes locally (e.g., in a JSON or CSV file).

### 2. 📊 Exploratory Data Analysis (EDA)

After collecting the data, run the EDA.ipynb to explore and prepare the jokes for the RAG pipeline.

This step includes:

- Data cleaning and formatting.
- Sentiment analysis and keyword extraction.
- Preparing the jokes for efficient retrieval in RAG.

### 3. 😜 Running Dad-GPT App

to start the Streamlit app, run:

```
streamlit run app.py
```

The app will:

- Display a form where you can type a prompt.
- Generate a creative dad joke using a local LLM via LangChain.
- Display a matching GIF using the Giphy API.

## 📁 Project Structure

```
├── app.py # Streamlit app for generating dad jokes
├── collect_dadjokes.py # Reddit PRAW data collector
├── eda.py # EDA and RAG preparation script
├── vector.py # Vector database setup
├── main.py # Terminal app
├── dad-gpt_icon.png # Logo
├── requirements.txt # Dependencies
├── cleaned_dadjokes.csv # Cleaned data
├── load_jokes.py # Script to collect top joke from reddit
├── data # Folder with csvs
├── .env # Environment variables (API keys)
└── README.md # This file
```

## 🤝 Contributing

Contributes are welcome!
If you have ideas, find bugs, or want to help expand this project, feel free to open an issue or submit a pull request.

## 🙌 Acknowledgements

- [**Streamlit**](https://streamlit.io/) – For making it easy to build beautiful, interactive web apps in Python.
- [**LangChain**](https://www.langchain.com/) – For enabling LLM-based pipelines and integration with local models.
- [**Ollama**](https://ollama.com/) – For running local LLMs like LLaMA, Mistral, etc., with simplicity and speed.
- [**Giphy Developers**](https://developers.giphy.com/) – For providing the GIF API that brings visual humor to the app.
- [**PRAW**](https://praw.readthedocs.io/) – For simple and powerful access to Reddit’s API, used to collect dad jokes.
- [**r/dadjokes**](https://www.reddit.com/r/dadjokes/) – For the treasure trove of community-sourced dad jokes.
- [**TechWithTim**](https://www.youtube.com/@TechWithTim) – For helpful tutorials and Python project guidance.
- [**ChatGPT**](https://openai.com/chatgpt) – For assisting in planning and refining project code, documentation and images.

<br>
<br>
Hope this project brings a smile to your face — happy coding! 🧡
