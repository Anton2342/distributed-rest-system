from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

PRODUCTS_SERVICE_URL = "http://127.0.0.1:8001"

app = FastAPI(title="Stock Service")


class Stock(BaseModel):
    productId: int
    quantity: int


# Hardcoded stock data
STOCK_DB = {
    1: 15,
    2: 0,
    3: 42,
}


@app.get("/stock/{product_id}", response_model=Stock)
async def get_stock(product_id: int):
    print(f"[Stock Service] GET /stock/{product_id} received")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCTS_SERVICE_URL}/products/{product_id}")

    if response.status_code == 404:
        print(f"[Stock Service] Product {product_id} does NOT exist")
        raise HTTPException(status_code=404, detail="Product does not exist")

    if response.status_code != 200:
        print(f"[Stock Service] Unexpected status from Products Service: {response.status_code}")
        raise HTTPException(status_code=502, detail="Error contacting Products Service")

    quantity = STOCK_DB.get(product_id, 0)
    print(f"[Stock Service] Returning stock for product {product_id}: quantity={quantity}")

    return Stock(productId=product_id, quantity=quantity)
