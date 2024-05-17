from fastapi import FastAPI, Path
import process_user
import products.process_products

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/get-item/{item_id}')
def get_item(
    item_id: int = Path(
        None,
        description="Fill with ID of the item you want to view")):

    search = list(filter(lambda x: x["id"] == item_id, products))

    if search == []:
        return {'Error': 'Item does not exist'}

    return {'Item': search[0]}
