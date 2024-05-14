from fastapi import FastAPI, Path
import process_user
import products.process_products

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
