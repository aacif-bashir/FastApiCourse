from fastapi import FastAPI, HTTPException, Request
from mockData import products
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home_page():
    return "This is the fastApi"
# Query params
@app.get("/greet")
def greet(request: Request):
    queryParams = dict(request.query_params)
    return {
        "greet": f"your name is {queryParams.get('name')} and your age is {queryParams.get('age')}"
    }


@app.get("/products")
def list_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id:int):
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/create_product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"detail": "Product created successfully"}

@app.delete("/product/product_id")
def delete_product(product_id):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deletedProduct= products.pop(index)
            return {
             f'success {deletedProduct}'
            }