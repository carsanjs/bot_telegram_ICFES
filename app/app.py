from fastapi import FastAPI
from api.api_v1.router import router
import os


app = FastAPI(
    title="API bot of telegram for ICFES",
    swagger_ui_parameters={"tryItOutEnabled": True},
    openapi_url=f"apicfes/openapi.json",
    description="description of",
    summary="implementation of",
    version="0.0.1",
)

app.include_router(router, prefix=["/endpoints"]) # Include router

@app.get("/", status_code=200, description="index")
def read_root():
    return ({
        "message": "Hello",
        "status": "200 OK"
    })

