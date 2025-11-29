from fastapi import FastAPI, HTTPException

app = FastAPI(title="Products Service")

# Prosta baza produktów w pamięci
products_db = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Phone", "price": 3200.00},
    3: {"id": 3, "name": "Mouse", "price": 120.00},
}

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product = products_db.get(product_id)
    if not product:
        print(f"[Products Service] Product {product_id} NOT found")
        raise HTTPException(status_code=404, detail="Product not found")

    print(f"[Products Service] Product {product_id} FOUND: {product}")
    return product
