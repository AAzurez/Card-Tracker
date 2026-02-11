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

@router.get("/grade/{graded_card}")
def get_grade(graded_card: str):

    cards_graded = []

    for card in FAKE_CARDS:
        if card["graded"] == True:
            cards_graded.append(card)

    if not cards_graded:
        raise HTTPException(status_code=404, detail="Set not found")

    return cards_graded

@router.get("/name/{card_name}")
def get_cards_name(card_name: str):

    same_card_name = []

    for card in FAKE_CARDS:
        if card["name"] == card_name:
            same_card_name.append(card)

    if not same_card_name:
        raise HTTPException(status_code=404, detail="Set not found")

    return same_card_name

@router.get("/price/{under_price_card}")
def get_price_under(under_price_card: int):

    under_price = []

    for card in FAKE_CARDS:
        for price in card["prices"].values():
            if price < under_price_card:
                under_price.append(card)

    if not under_price:
        raise HTTPException(status_code=404, detail="Set not found")

    return under_price