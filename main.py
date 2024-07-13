import logging

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello there!"}


app = FastAPI()


# @app.get('/keys')
# async def keys():
#     with


@app.post('/keys/log')
async def keys(request: Request):
    body = await request.body()
    body_str = body.decode()
    logging.info(body_str)
    return {"message": "ok"}


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
