# The code also supports Olama
import os
from langchain_community.llms import Ollama

def generate_smart_response(review: str, media: str):
    client = os.getenv("OLLAMA_CLIENT")
    llm = Ollama(model="llama3", base_url=client)
    prompt = f"""
        Given the below review about the media type {media}
        give the user a fun and interesting feedback on how well articulated their review are 

        {review}
    """
    return llm.invoke(prompt)

def prompt(prompt:str):
    client = os.getenv("OLLAMA_CLIENT")
    llm = Ollama(model="llama3", base_url=client)
    return llm.invoke(prompt)