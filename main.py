from typing import Optional, Union
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Fake database
my_items = [
    {
        "id": 1,
        "title": "Item 1",
        "content": "Item 1 content",
        "published": True,
        "rating": 5
    },
    {
        "id": 2,
        "title": "Item 2",
        "content": "Item 2 content",
        "published": True,
        "rating": 4
    }
]

def find_item(id):
    for item in my_items:
        if item["id"] == id:
            return item


# Schema Validation with Pydantic
class Item(BaseModel):
    title: str
    content: str
    published: bool = True # Valor por defecto (esto tiene el efecto de actuar como un campo opcional)
    rating: Optional[int] = None # Campo opcional

@app.get("/")
def read_root():
    return {"Message": "Hello World Again!!"}


@app.get("/items")
def read_items():
    return {"data": my_items}


@app.get("/items/{item_id}")
def read_item(item_id: int): # Al especificar el tipo, Fastapi parsea y genera validaciones automáticamente
    item = find_item(item_id)
    return {"item_detail": item}


# Instrucciones del video-tutorial de Sanjeev Thiyagarajan
@app.post("/items/new-item")
def create_item(new_item: Item):
    print(new_item) # Pydantic model
    new_item_dict = new_item.model_dump() # Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
    new_item_dict["id"] = randrange(0, 10000)
    my_items.append(new_item_dict)
    return { "new_item": new_item_dict}