from typing import List
from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from sqlalchemy import func
from .database import SessionLocal, engine
from datetime import datetime
from . import schemas, models, tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/api/v1/books', status_code=200, response_model=List[schemas.Book])
def get_all_books(author: str = None, publication_year: int = None, db: Session = Depends(get_db)):
    """
    Get list of all books stored in database.
    """
    try:
        query = db.query(models.Book)
        if author:
            query = query.filter(func.lower(models.Book.author)
                                 == func.lower(author))

        if publication_year:
            query = query.filter(
                models.Book.publication_year == publication_year)

        return query.all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/api/v1/books/create', status_code=201)
def add_new_book(new_book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Add a new book.
    Parameters: title: str, author: str, publication_year: int
    """

    if new_book.publication_year > datetime.now().year:
        raise HTTPException(
            status_code=400, detail="Year should not be greater than current year")

    try:
        book = models.Book(title=new_book.title, author=new_book.author,
                           publication_year=new_book.publication_year)
        db.add(book)
        db.commit()
        db.refresh(book)
        return {'message': 'Created new book successfully', 'new_book': book}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unable to create user")


@app.get('/api/v1/books/{book_id}/reviews', status_code=200, response_model=List[schemas.Review])
def get_all_reviews(book_id: int, db: Session = Depends(get_db)):
    """
    Get list of all review of a book.
    Parameters: book_id: int
    """
    try:
        book = db.query(models.Book).get(book_id)
        return book.reviews
    except Exception as e:
        raise HTTPException(status_code=404, detail="Unable to fetch reviews")


@app.post('/api/v1/books/{book_id}/reviews', status_code=201)
async def add_book_review(book_id: int, new_review: schemas.ReviewCreate, background_task: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Add review of a book.
    Parameters: book_id: int, review: str, rating: int
    """

    if new_review.rating < 0 or new_review.rating > 5:
        raise HTTPException(
            status_code=400, detail="Rating should be between 0 to 5")
    try:
        review = models.Review(
            book_id=book_id, review=new_review.review, rating=new_review.rating)
        db.add(review)
        db.commit()
        db.refresh(review)
        background_task.add_task(tasks.email_confirmation_task,
                                 message=f"New review for book id \"{book_id}\" is added.")
        return {
            'message': f'Created new review successfully for Book id: {book_id}',
            'review': review
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unable to create review")
