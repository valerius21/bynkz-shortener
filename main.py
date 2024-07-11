from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello there!"}


@app.get("/webtop")
async def webtop():
    redirect_url = ("https://gist.githubusercontent.com/valerius21/40d9055856e02f00acdb809ea3b36b5b/raw/acd2f1bae"
                    "1a2212"
                    "668e9a61a0dd10d0e5924e38c/webtop.sh")
    return RedirectResponse(redirect_url)
