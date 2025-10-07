from sqlalchemy.orm import Session
from sqlalchemy import and_
from app import models, schemas


def get_wishlist_by_user_and_product(db: Session, user_id: int, product_variation_id: int):
    return db.query(models.Wishlist).filter(
        and_(
            models.Wishlist.user_id == user_id,
            models.Wishlist.product_variation_id == product_variation_id
        )
    ).first

def get_wishlist_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Wishlist).filter(
        models.Wishlist.user_id == user_id
    ).offset(skip).limit(limit).all()

def get_wishlist_count_by_user(db: Session, user_id: int):
    return db.query(models.Wishlist).filter(
        models.Wishlist.user_id == user_id
    ).count()

def create_wishlist(db: Session, wishlist: schemas.WishlistCreate):
    db_wishlist = models.Wishlist(**wishlist.model_dump())
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist

def delete_wishlist(db: Session, wishlist_id: int):
    db_wishlist = db.query(models.Wishlist).filter(models.Wishlist.id == wishlist_id).first()
    if db_wishlist:
        db.delete(db_wishlist)
        db.commit()
    return db_wishlist

def delete_wishlist_by_user_and_product(db: Session, user_id: int, product_variation_id: int):
    db_wishlist = get_wishlist_by_user_and_product(db, user_id, product_variation_id)
    if db_wishlist:
        db.delete(db_wishlist)
        db.commit()
    return db_wishlist