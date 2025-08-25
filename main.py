from fastapi import FastAPI

app = FastAPI(title="API da Suzane")

@app.get("/")
def helloWorld():
    return {"message": "Hello World!"}