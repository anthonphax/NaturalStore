from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Product(BaseModel):
    name: str
    description: str
    cost: float
    price: float
    amount: int
    purchased: int
    sold: int
    weight: float
    manufacturer: str
    group: str
    subgroup: Optional[str] = None


products = [
    {'id': 1, 'name': 'coffee', 'price': 2.5},
    {'id': 2, 'name': 'cake', 'price': 10},
    {'id': 3, 'name': 'tea', 'price': 3.2},
    {'id': 4, 'name': 'croissant', 'price': 5.79}
]

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

@app.get("/")
async def root():
    return {"TESTE": "Hello World"}


@app.get('/products')
def list_products():    
    return {'products': products}


@app.get('/products-name')
def get_item(name: Optional[str] = None):
    search = [prod for prod in products if prod["name"] == name]
    if not search:
        return {'item': 'Does not exist'}
    return {'products': search[0]}


@app.post('/products/new/{item_id}')
def create_item(item_id: int, item: Product):
    if any(prod["id"] == item_id for prod in products):
        return {'Error': 'Item exists'}
    item = item.dict()
    item['id'] = item_id
    products.append(item)
    return item


@app.put('/products/update/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    search = [prod for prod in products if prod["id"] == item_id]
    if not search:
        return {'Item': 'Does not exist'}
    if item.name is not None:
        search[0]['name'] = item.name
    if item.price is not None:
        search[0]['price'] = item.price
    return {'products': search}


@app.delete('/products/delete/{item_id}')
def delete_item(item_id: int):
    search = [prod for prod in products if prod["id"] == item_id]
    if not search:
        return {'Item': 'Does not exist'}
    products.remove(search[0])
    return {'Message': 'Item deleted successfully'}
