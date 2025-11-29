from fastapi import FastAPI, HTTPException

app = FastAPI(title="Stock Service")

stock_db = {
    1: {"productId": 1, "quantity": 15},
    2: {"productId": 2, "quantity": 8}
}

@app.get("/stock/{product_id}")
async def get_stock(product_id: int):
    if product_id in stock_db:
        return stock_db[product_id]
    raise HTTPException(status_code=404, detail="Product does not exist")
