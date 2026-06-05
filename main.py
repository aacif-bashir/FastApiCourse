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
def get_product(product_id: int):
    for OneProduct in products:
        if OneProduct.get("id") == product_id:
            return OneProduct

    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/create_product")
def create_product(product_data: ProductDTO):
    new_product = product_data.model_dump()
    products.append(new_product)
    return new_product

@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO,product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            raise HTTPException(status_code=200, detail=f"Successfully update the product with id {product_id}")
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            raise HTTPException(status_code=200, detail={
                "message": "Product deleted successfully",
                "product": f"{deleted_product}"
            })
    raise HTTPException(status_code=404, detail="Product not found")
        