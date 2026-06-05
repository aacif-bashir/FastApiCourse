from fastapi import FastAPI, HTTPException, Request
from mockData import products

app = FastAPI()

@app.get("/")
def home_page():
    return "This is the fastApi"
# Query params
@app.get("/greet")
def greet(request: Request):
    queryParams = dict(request.query_params)
    return {
        "greet": f"your name is {queryParams.get("name")} and your age is {queryParams.get("age")}"
    }


@app.get("/products")
def list_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id:int):
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
    return HTTPException(status_code=404, detail="Product not fount")