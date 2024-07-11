from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello there!"}


app = FastAPI()


@app.get("/webtop")
async def webtop():
    with open("webtop.sh", "r") as f:
        text_content = f.read()
    return PlainTextResponse(text_content)
