from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import *
from db import models
from db.database import session, engine
import uvicorn


app = FastAPI(title='Books API')



models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()



# book
@app.post('/books')
async def create_book(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.price = book.price

    db.add(book_model)
    db.commit()

    return book


@app.get('/books')
async def read_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()


@app.put('/books/{book_id}')
async def read_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Book with id {book_id} does not exist'
        )
    book_model.title = book.title
    book_model.author = book.author
    book_model.price = book.price

    db.add(book_model)
    db.commit()

    return book


@app.delete('/books/{book_id}')
async def delete_book(book_id: int, db: Session = Depends(get_db)): 
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Book with id {book_id} does not exist'
        )
    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()
    return f'Deleted book with id {book_id}'

















# tag
@app.post('/tags')
async def create_tag(tag: Tag, db: Session = Depends(get_db)):
    tag_model = models.Tags()
    tag_model.name = tag.name

    db.add(tag_model)
    db.commit()

    return tag


@app.get('/tags')
async def read_tag(db: Session = Depends(get_db)):
    return db.query(models.Tags).all()


@app.put('/tags/{tag_id}')
async def read_tag(tag_id: int, tag: Tag, db: Session = Depends(get_db)):
    tag_model = db.query(models.Tags).filter(models.Tags.id == tag_id).first()
    if tag_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Tag with id {tag_id} does not exist'
        )
    tag_model.name = tag.name

    db.add(tag_model)
    db.commit()

    return tag


@app.delete('/tags/{tag_id}')
async def delete_tag(tag_id: int, db: Session = Depends(get_db)):   
    book_model = db.query(models.Tags).filter(models.Tags.id == tag_id).first()
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Tag with id {tag_id} does not exist'
        )
    db.query(models.Tags).filter(models.Tags.id == tag_id).delete()
    db.commit()
    return f'Deleted tag with id {tag_id}'


# category
@app.post('/cat')
async def create_cat(cat: Category, db: Session = Depends(get_db)):
    cat_model = models.Categorys()
    cat_model.name = cat.name

    db.add(cat_model)
    db.commit()

    return cat


@app.get('/cat')
async def read_cat(db: Session = Depends(get_db)):
    return db.query(models.Categorys).all()


@app.put('/cat/{cat_id}')
async def read_cat(cat_id: int, cat: Tag, db: Session = Depends(get_db)):
    cat_model = db.query(models.Tags).filter(models.Tags.id ==  cat_id).first()
    if cat_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Cat with id {cat_id} does not exist'
        )
    cat_model.name = cat.name

    db.add(cat_model)
    db.commit()

    return cat


@app.delete('/cat/{cat_id}')
async def delete_cat(cat_id: int, db: Session = Depends(get_db)):   
    cat_model = db.query(models.Categorys).filter(models.Tags.id == cat_id).first()
    if cat_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Cat with id {cat_id} does not exist'
        )
    db.query(models.Tags).filter(models.Tags.id == cat_id).delete()
    db.commit()
    return f'Deleted cat with id {cat_id}'



# author
@app.post('/author')
async def create_author(author: Author, db: Session = Depends(get_db)):
    author_model = models.Authors()
    author_model.name = author.name

    db.add(author_model)
    db.commit()

    return author


@app.get('/author')
async def read_author(db: Session = Depends(get_db)):
    return db.query(models.Authors).all()


@app.put('/author/{author_id}')
async def read_author(author_id: int, author: Author, db: Session = Depends(get_db)):
    author_model = db.query(models.Authors).filter(models.Authors.id ==  author_id).first()
    if author_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Author with id {author_model} does not exist'
        )
    author_model.name = author.name

    db.add(author_model)
    db.commit()

    return author


@app.delete('/author/{author_id}')
async def delete_author(author_id: int, db: Session = Depends(get_db)):   
    author_model = db.query(models.Authors).filter(models.Authors.id == author_id).first()
    if author_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'Author with id {author_id} does not exist'
        )
    db.query(models.Authors).filter(models.Authors.id == author_id).delete()
    db.commit()
    return f'Deleted author with id {author_id}'



if __name__ == '__main__':
    uvicorn.run('main:app', port=5050, reload=True)