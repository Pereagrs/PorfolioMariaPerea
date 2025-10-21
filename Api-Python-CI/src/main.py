from fastapi import FastAPI

app = FastAPI(title="Mi API de ejemplo")

@app.get("/")
def read_root():
    return {"message": "Hola, María! Esta es mi API desde FastAPI."}

@app.get("/suma")
def suma(a: int, b: int):
    return {"result": a + b}
