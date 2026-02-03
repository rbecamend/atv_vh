from fastapi import FastAPI

app = FastAPI(title="api de soma")

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/soma")
def sumar_numeros(a: int, b: int):
    return {"resultado": a + b}