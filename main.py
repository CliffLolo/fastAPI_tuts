from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Cliff": "Lolo"}


@app.get("/items/{item_id}")
def read_item(item_id: int, optional_parameter: Union[str, None] = None):
    return {"item_id": item_id, "optional_parameter": optional_parameter}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}