from typing import Optional, Union
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# Schema Validation with Pydantic
class Item(BaseModel):
    title: str
    content: str
    published: bool = True # Valor por defecto (esto tiene el efecto de actuar como un campo opcional)
    rating: Optional[int] = None # Campo opcional

@app.get("/")
def read_root():
    return {"Message": "Hello World Again!!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Instrucciones del video-tutorial de Sanjeev Thiyagarajan
@app.post("/items/new-item")
def create_item(new_item: Item):
    print(new_item) # Pydantic model
    print(new_item.model_dump()) # Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
    print(new_item.model_dump_json()) # Generates a JSON representation of the model using Pydantic's to_json method.
    return { "new_item": new_item}