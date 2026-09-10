from fastapi import Response, APIRouter
from model.product_model import Product

from controller.product_controller import (
    create_product_controller,
    get_product_controller,
    get_product_controller_id,
    update_product_controller,
    delete_product_controller
)


productrouter = APIRouter(
    prefix="/products",
    tags=["products"]
)


# CREATE PRODUCT
@productrouter.post("/")
async def create_product(
    product: Product,
    response: Response
):
    return await create_product_controller(
        product,
        response
    )


# GET ALL PRODUCTS
@productrouter.get("/getproducts")
async def get_products(
    response: Response
):
    return await get_product_controller(response)


# GET PRODUCT BY ID
@productrouter.get("/getproduct/{productid}")
async def get_product(
    productid: int,
    response: Response
):
    return await get_product_controller_id(
        productid,
        response
    )


# UPDATE PRODUCT
@productrouter.put("/updateproduct/{productid}")
async def update_product(
    productid: int,
    product: Product,
    response: Response
):
    return await update_product_controller(
        productid,
        product,
        response
    )


# DELETE PRODUCT
@productrouter.delete("/deleteproduct/{productid}")
async def delete_product(
    productid: int,
    response: Response
):
    return await delete_product_controller(
        productid,
        response
    )