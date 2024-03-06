from pydantic import BaseModel
from typing import List


class ReviewBase(BaseModel):
    review: str
    rating: int


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_model = True


class BookBase(BaseModel):
    title: str
    author: str
    publication_year: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    # reviews: List[Review]

    class Config:
        orm_model = True
