from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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


def find_index(id):
    for item in my_items:
        if item["id"] == id:
            return my_items.index(item)


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
    if not item:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Item with id {item_id} was not found"
        )
    return {"item_detail": item}


# Instrucciones del video-tutorial de Sanjeev Thiyagarajan
@app.post("/items/new-item", status_code=status.HTTP_201_CREATED)
def create_item(new_item: Item):
    print(new_item) # Pydantic model
    new_item_dict = new_item.model_dump() # Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
    new_item_dict["id"] = randrange(0, 10000)
    my_items.append(new_item_dict)
    return { "new_item": new_item_dict}


# Temporal delete implementation with the fake database
@app.delete("/items/{id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_item(id: int):
    index = find_index(id)
    if index == None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f"Item with id {id} does not exist"
        )
    my_items.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Temporal update implementation with the fake database
@app.put("/items/{id}")
def update_item(id: int, item: Item):
    index = find_index(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {id} does not exist"
        )
    
    item_dict = item.model_dump()
    item_dict["id"] = id
    my_items[index] = item_dict

    return {"updated_item": my_items[index]}