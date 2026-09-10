from fastapi import FastAPI

from router.product_router import productrouter


app = FastAPI()


app.include_router(productrouter)