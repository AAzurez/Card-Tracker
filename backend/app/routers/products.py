from fastapi import APIRouter, HTTPException
from backend.app.data.products import FAKE_PRODUCTS

router = APIRouter(
    prefix="/product",
    tags=["product"], #WHAT DOES THIS DO?
)

@router.get("/")
def get_all_product():
    return FAKE_PRODUCTS
    

@router.get("/{product}")
def get_specific_product(name_product: str):
    for product in FAKE_PRODUCTS:
        if card["name"] == name_product:
            return product

    if not name_product:
        raise HTTPException(status_code=404, detail="Box not found")
    
@router.get("/sets/{product}")
def get_set(box_type: str):

    products = []

    for box in FAKE_PRODUCTS:
        if box["box_type"] == box_type:
            products.append(box)

    if not products:
        raise HTTPException(status_code=404, detail="Products not found")
    return products