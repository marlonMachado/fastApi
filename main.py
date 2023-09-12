from fastapi import FastAPI
from router.router import user

app = FastAPI()
# @app.get("/")
# def root():
#     return "hi domun"

app.include_router(user)