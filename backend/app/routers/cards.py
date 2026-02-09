from fastapi import APIRouter, HTTPException
from backend.app.data.cards import FAKE_CARDS

router = APIRouter(
    prefix="/card",
    tags=["cards"],
)

@router.get("/")
def list_cards():
    return FAKE_CARDS

@router.get("/{card_id}")
def get_card(card_id: str):
    for card in FAKE_CARDS:
        if card["id"] == card_id:
            return card
    raise HTTPException(status_code=404, detail="Card not found")

@router.get("/sets/{card_set}")
def get_set(card_set: str):

    cards_in_set = []

    for card in FAKE_CARDS:
        if card["set"] == card_set:
            cards_in_set.append(card)

    if not cards_in_set:
        raise HTTPException(status_code=404, detail="Set not found")

    return cards_in_set