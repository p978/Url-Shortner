import string,random
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class url_data(BaseModel):
    previous_url : str
@app.get("/")
async def root():
    return ("You probably should go to the docs")
@app.post("/urls/")
async def get_url(urls:url_data):
    return {"Shorted url is": "http://127.0.0.1:8000/"+''.join(random.choices(string.ascii_letters, k=4))}