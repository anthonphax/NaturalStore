from fastapi import FastAPI, HTTPException
import models.products

app = FastAPI()

@app.get('/products')
def list_products():    
    return {'products': products}


@app.get('/products-name')
def get_item(name: Optional[str] = None):

    search = list(filter(lambda x: x["name"] == name, products))

    if search == []:
        return {'item': 'Does not exist'}

    return {'Item': search[0]}


@app.post('/products/new/{item_id}')
def create_item(item_id: int, item: Item):

    search = list(filter(lambda x: x["id"] == item_id, products))

    if search != []:
        return {'Error': 'Item exists'}

    item = item.dict()
    item['id'] = item_id

    products.append(item)
    return item


@app.put('/products/update/{item_id}')
def update_item(item_id: int, item: UpdateItem):

    search = list(filter(lambda x: x["id"] == item_id, products))

    if search == []:
        return {'Item': 'Does not exist'}

    if item.name is not None:
        search[0]['name'] = item.name

    if item.price is not None:
        search[0]['price'] = item.price

    return search


@app.delete('/products/delete/{item_id}')
def delete_item(item_id: int):
    search = list(filter(lambda x: x["id"] == item_id, products))

    if search == []:
        return {'Item': 'Does not exist'}

    for i in range(len(products)):
        if products[i]['id'] == item_id:
            del products[i]
            break
    return {'Message': 'Item deleted successfully'}