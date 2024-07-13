from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"TODO": "Make appointment for that 'V' tattoo"}


@app.get("/key")
async def key(request: Request):
    with open("files/ed25519.pub", "r") as f:
        text_content = f.read()
    return PlainTextResponse(text_content)


@app.get("/webtop")
async def webtop():
    with open("files/webtop/webtop.sh", "r") as f:
        text_content = f.read()
    return PlainTextResponse(text_content)


@app.get("/webtop/docker-compose.yml")
async def webtop_docker():
    with open("files/webtop/docker-compose.yml", "r") as f:
        text_content = f.read()
    return PlainTextResponse(text_content)
