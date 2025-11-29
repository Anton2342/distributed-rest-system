from fastapi import FastAPI, HTTPException

app = FastAPI(title="Products Service")

products_db = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Phone", "price": 3200.00}
}

@app.get("/products/{id}")
async def get_product(id: int):
    if id in products_db:
        return products_db[id]
    raise HTTPException(status_code=404, detail="Product not found")
