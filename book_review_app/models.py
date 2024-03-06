from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    publication_year = Column(Integer)

    reviews = relationship("Review", back_populates="books")


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    review = Column(String)
    rating = Column(Integer, default=1)
    book_id = Column(Integer, ForeignKey("books.id"))

    books = relationship("Book", back_populates="reviews")
