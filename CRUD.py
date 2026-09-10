from fastapi import FastAPI,Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Product(BaseModel):
    id : Optional[int] = None
    name : str
    price : float
    description : str

products = []
id = 0

@app.post("/")
def create_product(product:Product, response:Response):
    global id
    try:
        id += 1
        product.id = id
        products.append(product)
        response.status_code = 201
        return{'isSuccess' : True, 'message': "Product created successfully"}
    except Exception as e:
        response.status_code = 500
        return{"message" : "Error Creating product",'isSuccess': False}
    
# GET ALL PRODUCTS
@app.get("/products")
def get_products(response: Response):
    print("data -> ", products)
    response.status_code = 200
    return {
        "message": "Products get successfully!",
        "product": products
    }
    
#Get single record
@app.get("/products/{productid}")
def get_product(productid: int, response: Response):
    try:
        
        for product in  products:
            if product.id == productid:
                response.status_code=200
                return{'product' : product,'isSuccess': True}
            response.status_code = 404
            return{"message" : "Product not found", "isSuccess":False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{"message" : "Error fetching product","product" : False}
    
#update product
@app.put('/product/{productid}')
def updateproduct(productid, product:Product,response:Response):
    try:
        idx = 0
        for index in range (0,len(products),1):
            if products[index] == productid:
                idx = index
        products[idx] = product
    except Exception as e:
        response.status_code = 500
        return{'message': "Error fetching product",'isSuccess': False}