from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

def get_current_user():
    """JWT token validation (sadə versiya)"""
    # Real tətbiqdə JWT token validate edəcəksiniz
    return {"user_id": 1}  # Mock user

def get_db_session(db: Session = Depends(get_db)):
    return db