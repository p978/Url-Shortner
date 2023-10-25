import string,random
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
app = FastAPI()
# Connect to my sql Database
class url_data(BaseModel):
    previous_url : str
# The root
@app.get("/")
async def root():
    return ("You probably should go to the docs")
@app.post("/urls/")
async def get_url(urls:url_data):
    res = ''.join(random.choices(string.ascii_letters, k=4))
    @app.get("/"+res)
    async def redirect_typer(u:url_data):
        return u.previous_url()
    return {"Shorted url is": "http://127.0.0.1:8000/"+res}