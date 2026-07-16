from fastapi import FastAPI

app = FastAPI(title="Hello API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Hello"}


@app.get("/hello")
def hello():
    return {"message": "Hello"}


@app.get("/eugenia")
def eugenia():
    return {"message": "Hi, I am Eugenia"}
