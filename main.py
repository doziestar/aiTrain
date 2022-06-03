from typing import Union

import openai
import requests
from fastapi import FastAPI

openai.api_key = "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"

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# create open ai that will generate programming memes
@app.get("/openai/{text}")
async def open_ai_generate_meme(text: str):
    """
    Generate a meme using open ai
    @param text: text to be used in the meme
    @return: meme
    @rtype: str
    """
    # response = requests.get(f"https://api.openai.com/api/v1/?model_name=programming_memes&prefix={text}")
    response = openai.Completion.create(engine="davinci", prompt=text)
    return response.choices[0].text
