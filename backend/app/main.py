from fastapi import FastAPI
from backend.app.routers.cards import router as card_router
from backend.app.routers.products import router as product_router

app = FastAPI(title = "WIP---Website")

app.include_router(card_router)
app.include_router(product_router)

@app.get("/")
def root():
    return {"message": "API Running!"}