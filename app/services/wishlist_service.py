from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import crud, schemas, events


class WishlistService:
    def __init__(self, db: Session):
        self.db = db

    async def add_to_wishlist(self, wishlist_create: schemas.WishlistCreate):
        existing = crud.get_wishlist_by_user_and_product(
            self.db,
            wishlist_create.user_id,
            wishlist_create.product_variation_id
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product already in wishlist"
            )
        
        wishlist = crud.create_wishlist(self.db, wishlist_create)

        await events.event_publisher.publish_event("wishlist.deleted", {
            "wishlist_id": wishlist.id,
            "user_id": wishlist.user_id,
            "product_variation_id": wishlist.product_variation_id
        })

        return wishlist
    
    def get_user_wishlist(self, user_id: int, skip: int = 0, limit: int = 100):
        items = crud.get_wishlist_by_user(self.db, user_id, skip, limit)
        total = crud.get_wishlist_count_by_user(self.db, user_id)
        
        return {
            "items": items,
            "total": total
        }