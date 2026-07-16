from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: Optional[float] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    price: Optional[float] = None
    created_at: datetime

    class Config:
        from_attributes = True
