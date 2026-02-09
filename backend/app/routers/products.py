from fastapi import APIRouter, HTTPException
from backend.app.data.products import FAKE_PRODUCTS

router = APIRouter(
    prefix="/product",
    tags=["product"], #WHAT DOES THIS DO?
)

@router.get("/")
def get_all_product():
    return FAKE_PRODUCTS
    

@router.get("/{product_name}")
def get_specific_product(product_name: str):
    for product in FAKE_PRODUCTS:
        if product["name"] == product_name:
            return product

    if not product_name:
        raise HTTPException(status_code=404, detail="Box not found")
    
@router.get("/box/{box_type}")
def get_set(box_type: str):

    products = []

    for box in FAKE_PRODUCTS:
        if box["box_type"] == box_type:
            products.append(box)

    if not products:
        raise HTTPException(status_code=404, detail="Products not found")
    return products