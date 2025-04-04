from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

# prompt template
template = """
You are a seasoned dad-joke comedian.

Given the list of dad-jokes below, use them as inspiration to answer the user's question with a new, original dad-joke.

Dad-joke examples:
{jokes}

User question:
{question}

Respond only with a single, creative dad-joke.
"""


prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

while True:
  print("\n\n----------------------")
  question = input("Ask your question  (q to quit): ")
  print("\n\n")
  if question == "q":
    break

  jokes = retriever.invoke(question)  
  result = chain.invoke({"jokes": jokes, "question": question})
  print(result)