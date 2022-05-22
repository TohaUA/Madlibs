from fastapi import FastAPI

from app import bl
from app import constants

app = FastAPI()


@app.get("/madlib", response_model=str)
async def say_hello():
    words = await bl.get_words()
    return f'It was a {words[constants.WordType.ADJECTIVE]} day. ' \
           f'I went downstairs to see if I could {words[constants.WordType.VERB]} dinner. ' \
           f'I asked, "Does the stew need fresh {words[constants.WordType.NOUN]}?"'
