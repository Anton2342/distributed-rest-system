from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="Stock Service")

# Adres serwisu produktów
PRODUCTS_SERVICE_URL = "http://127.0.0.1:8001"

# Prosta baza stanów magazynowych w pamięci
stock_db = {
    1: {"productId": 1, "quantity": 15},
    2: {"productId": 2, "quantity": 8},
    3: {"productId": 3, "quantity": 0},
}

@app.get("/stock/{product_id}")
async def get_stock(product_id: int):
    print(f"[Stock Service] GET /stock/{product_id} received")

    # 1. Sprawdzamy w Serwisie Produktów, czy produkt istnieje
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{PRODUCTS_SERVICE_URL}/products/{product_id}")
        except httpx.RequestError:
            # Problem z połączeniem z Serwisem Produktów
            raise HTTPException(status_code=500, detail="Products Service unavailable")

    if response.status_code == 404:
        print(f"[Stock Service] Product {product_id} does NOT exist")
        raise HTTPException(status_code=404, detail="Product does not exist")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error in Products Service")

    # 2. Produkt istnieje – zwracamy stan magazynowy
    stock = stock_db.get(product_id)
    if not stock:
        # Produkt istnieje, ale nie ma go w magazynie
        stock = {"productId": product_id, "quantity": 0}

    print(f"[Stock Service] Returning stock for product {product_id}: quantity={stock['quantity']}")
    return stock
