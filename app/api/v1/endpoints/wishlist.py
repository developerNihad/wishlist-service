from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app import schemas, services
from app.dependencies import get_db_session, get_current_user
from services import wishlist_service


router = APIRouter()


@router.post("/wishlist", response_model=schemas.Wishlist)
async def add_to_wishlist(
    wishlist: schemas.WishlistCreate,
    db: Session = Depends(get_db_session),
    current_user: dict = Depends(get_current_user)
):
    service = services.WishlistService(db)
    return await service.add_to_wishlist(wishlist)


@router.delete("/wishlist/{product_variation_id}")
async def remove_from_wishlist(
    product_variation_id: int,
    db: Session = Depends(get_db_session),
    current_user: dict = Depends(get_current_user)
):
    service = services.WishlistService(db)
    await service.remove_from_wishlist(current_user["user_id"], product_variation_id)
    return {"message": "Item removed from wishlist"}

@router.get("/wishlist", response_model=schemas.WishlistList)
def get_user_wishlist(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db_session),
    current_user: dict = Depends(get_current_user)
):
    service = services.WishlistService(db)
    return service.get_user_wishlist(current_user["user_id"], skip, limit)