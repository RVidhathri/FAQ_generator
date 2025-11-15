from langchain.prompts import PromptTemplate  # type: ignore
from langchain_groq import ChatGroq  # type: ignore
import os

def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

zero_shot_prompt = load_prompt("prompts/few_shot.txt")

def generate_faq(text):

    template = PromptTemplate(
        input_variables=["document"],
        template=zero_shot_prompt
    )

    llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)


    chain = template | llm
    result = chain.invoke({"document": text})

    return result.content
