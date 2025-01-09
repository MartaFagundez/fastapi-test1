from typing import Union
from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello World Again!!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Instrucciones del video-tutorial de Sanjeev Thiyagarajan
@app.post("/items/new-item")
def create_item(payload: dict = Body(...)):
    print(payload)
    return {f"title: {payload["title"]}, content: {payload["content"]}"}