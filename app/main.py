from fastapi import FastAPI

app = FastAPI(title="CI/CD Practice App")


@app.get("/")
def read_root():
    return {"message": "Hello, CI/CD!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}
