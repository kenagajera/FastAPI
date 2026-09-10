from fastapi import Response
from model.product_model import Product
from dbConnect import productCollection


products = []
id = 0


# CREATE PRODUCT

async def create_product_controller(product: Product, response: Response):
    global id

    try:
        # id += 1
        
        # product.id = id
        # products.append(product)
        
        # print("Product created:", product)
        # print("Products:", products)
        
        # response.status_code = 201

        # Find last product ID
        last_product = await productCollection.find_one(
            {"id": {"$type": "int"}},
            sort=[("id", -1)]
        )

        if last_product:
            new_id = last_product["id"] + 1
        else:
            new_id = 1

        product.id = new_id

        await productCollection.insert_one(
            product.model_dump()
        )

        response.status_code = 201

        return {
            "isSuccess": True,
            "product": product,
            "message": "Product created successfully"
        }

    except Exception as e:
        print(e)

        response.status_code = 500

        return {
            "message": "Error creating product",
            "error": str(e),
            "isSuccess": False
        }


# GET ALL PRODUCTS

async def get_product_controller(response: Response):
    try:

        # print("data -> ", products)

        # response.status_code = 200
        # return {
        #     "message": "Products get successfully!",
        #     "product": products
        # }

        print("in get")

        productss = []

        async for product in productCollection.find():

            print(product)

            productss.append(Product(**product))

        response.status_code = 200

        return {
            "message": "Products get successfully!",
            "products": productss,
            "isSuccess": True
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error fetching products",
            "error": str(e),
            "isSuccess": False
        }


# GET PRODUCT BY ID

async def get_product_controller_id(
    productid: int,
    response: Response
):
    try:

        # for product in products:

        #     if product.id == productid:

        #         response.status_code = 200

        #         return {
        #             "product": product,
        #             "isSuccess": True
        #         }

        # response.status_code = 404

        # return {
        #     "message": "Product not found",
        #     "isSuccess": False
        # }


        product = await productCollection.find_one(
            {"id": productid}
        )

        if product is None:

            response.status_code = 404

            return {
                "message": "Product not found",
                "isSuccess": False
            }

        response.status_code = 200

        return {
            "product": Product(**product),
            "isSuccess": True
        }

    except Exception as e:

        print("ERROR:", e)

        response.status_code = 500

        return {
            "message": "Error fetching product",
            "error": str(e),
            "isSuccess": False
        }


# UPDATE PRODUCT

async def update_product_controller(
    productid: int,
    product: Product,
    response: Response
):
    try:

        # for old_product in products:

        #     if old_product.id == productid:

        #         old_product.name = product.name
        #         old_product.price = product.price
        #         old_product.description = product.description

        #         response.status_code = 200

        #         return {
        #             "message": "Product updated successfully",
        #             "product": old_product,
        #             "isSuccess": True
        #         }

        # response.status_code = 404

        # return {
        #     "message": "Product not found",
        #     "isSuccess": False
        # }

        result = await productCollection.update_one(
            {"id": productid},
            {
                "$set": {
                    "name": product.name,
                    "price": product.price,
                    "description": product.description
                }
            }
        )

        if result.matched_count == 0:

            response.status_code = 404

            return {
                "message": "Product not found",
                "isSuccess": False
            }

        updated_product = await productCollection.find_one(
            {"id": productid}
        )

        response.status_code = 200

        return {
            "message": "Product updated successfully",
            "product": Product(**updated_product),
            "isSuccess": True
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error updating product",
            "error": str(e),
            "isSuccess": False
        }


# DELETE PRODUCT

async def delete_product_controller(
    productid: int,
    response: Response
):
    try:

        # for product in products:

        #     if product.id == productid:

        #         products.remove(product)

        #         response.status_code = 200

        #         return {
        #             "message": "Product deleted successfully",
        #             "isSuccess": True
        #         }

        # response.status_code = 404

        # return {
        #     "message": "Product not found",
        #     "isSuccess": False
        # }

        result = await productCollection.delete_one(
            {"id": productid}
        )

        if result.deleted_count == 0:

            response.status_code = 404

            return {
                "message": "Product not found",
                "isSuccess": False
            }

        response.status_code = 200

        return {
            "message": "Product deleted successfully",
            "isSuccess": True
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error deleting product",
            "error": str(e),
            "isSuccess": False
        }