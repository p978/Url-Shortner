import string,random,models
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
# Connect to my sql Database
from database import *
models.Base.metadata.create_all(bind=engine)
class url_data(BaseModel):
    previous_url : str
# The root
@app.get("/")
async def root():
    return ("You probably should go to the docs")
@app.post("/urls/")
async def get_url(urls:url_data):
    global res
    res = ''.join(random.choices(string.ascii_letters, k=4))
    
    return {"Shorted url is": "http://127.0.0.1:8000/"+res}