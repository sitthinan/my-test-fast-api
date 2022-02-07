from fastapi import FastAPI
from routers import product, money
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware


middleware = [(Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*']))]


app = FastAPI(middleware=middleware)



app.include_router(product.router)
app.include_router(money.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}