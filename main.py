import logging
import os

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello there!"}


app = FastAPI()


@app.post("/keys/save")
async def keys(file: UploadFile = File(...)):
    contents = await file.read()
    logging.info(contents.decode())

    with open(os.path.join('files', file.filename), 'wb') as f:
        f.write(contents)

    return JSONResponse(content={"filename": file.filename})


@app.get("/keys/show/{filename}")
async def keys(filename: str):
    with open(os.path.join('files', filename), 'rb') as f:
        contents = f.read()

    return PlainTextResponse(contents.decode())


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
