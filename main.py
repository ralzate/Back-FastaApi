# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    id: int
    name: str
    price: float

products: List[Product] = []

@app.get("/api/products", response_model=List[Product])
def get_products():
    return products

@app.post("/api/products", response_model=Product)
def create_product(product: Product):
    for produc in products:
        if produc.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists")
    products.append(product)
    return product

