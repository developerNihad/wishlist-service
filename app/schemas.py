from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class WishlistBase(BaseModel):
    user_id: int
    product_variation: int


class WishlistCreate(WishlistBase):
    pass


class WishlistUpdate(BaseModel):
    pass 


class Wishlist(WishlistBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class WishlistList(BaseModel):
    items: list[Wishlist]
    total: int