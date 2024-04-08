from fastapi import FastAPI, Depends
from db.models import *
from db.database import session, engine
import uvicorn
from sqlalchemy.orm import Session
from schemas import PostCreate, TagCreate, AuthorCreate, CatCreate
from crud import post_create, tag_create, author_create, cat_create, comment_create


Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()

@app.post('/create/')
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_create(db=db, post=post)


@app.get('/read/')
async def read_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@app.post('/tag/')
async def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return tag_create(db=db, tag=tag)


@app.post('/cat/')
async def create_cat(cat: CatCreate, db: Session = Depends(get_db)):
    return cat_create(db=db, cat=cat)


@app.post('/author/')
async def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_create(db=db, author=author)


@app.get('/read-tag/')
async def read_tag(db: Session = Depends(get_db)):
    return db.query(Tag).all()


@app.get('/read-cat/')
async def read_cat(db: Session = Depends(get_db)):
    return db.query(Category).all()


@app.get('/read-author/')
async def read_author(db: Session = Depends(get_db)):
    return db.query(Author).all()
if __name__ == '__main__':
    uvicorn.run('main:app', port=5050, reload=True)


# 