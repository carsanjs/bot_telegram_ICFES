from fastapi import FastAPI
import os


app = FastAPI()

@app.get("/")
def read_root():
    return ({
        "message": "Hello",
        "status": "200 OK"
    })
