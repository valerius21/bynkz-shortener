import logging
import os

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"TODO": [
        {"item": "Make appointment for that 'V' tattoo", "status": "TODO"},
    ]}


app = FastAPI()


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
