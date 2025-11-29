from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Products Service")


class Product(BaseModel):
    id: int
    name: str
    price: float


# "Na sztywno" – база продуктов в памяти
PRODUCTS_DB = {
    1: Product(id=1, name="Laptop", price=4500.00),
    2: Product(id=2, name="Smartphone", price=2500.00),
    3: Product(id=3, name="Headphones", price=350.00),
}


@app.get("/products/{id}", response_model=Product)
async def get_product(id: int):
    print(f"[Products Service] GET /products/{id} received")
    product = PRODUCTS_DB.get(id)
    if not product:
        print(f"[Products Service] Product {id} NOT FOUND")
        raise HTTPException(status_code=404, detail="Product not found")
    print(f"[Products Service] Product {id} FOUND: {product}")
    return product
