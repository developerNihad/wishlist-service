from sqlalchemy import Column, BigInteger, DateTime, Text, UniqueConstraint
from sqlalchemy.sql import func
from app.database import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=True, index=True)
    product_variation_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint('user_id', 'product_variation_id', name='unique_user_product'), )

