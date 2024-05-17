from fastapi import FastAPI, HTTPException

app = FastAPI()

class Product:
    def __init__(self, name, description, cost, price, amount, purchased, sold, weight, manufacturer, group, subgroup=None ):
        self.name = name
        self.description = description
        self.cost = cost
        self.price = price
        self.amount = amount
        self.purchased = purchased
        self.sold = sold
        self.weight = weight
        self.manufacturer = manufacturer
        self.group = group
        self.subgroup = subgroup


class ProductFactory:
    @staticmethod
    def create_Product(Product_type: str) -> Product:
        pass

@app.get("/products")
async def root():
    return {"All products": "Hello World"}

@app.get("/{Group}/products")
async def root():
    return {"Group Products": "Hello World"}

