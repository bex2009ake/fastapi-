from sqlalchemy.orm import Session
from db.models import Post, Tag, Author, Category, Comment
from schemas import PostCreate, AuthorCreate, TagCreate, CatCreate, CommentCreate
import os


def post_create(db: Session, post: PostCreate):
    tags = [i for i in post.tags]
    model = Post(**post.dict(exclude={'tags'}))
    model.tags = tags
    db.add(model)
    db.commit()
    db.refresh(model)
    return post.__dict__




def author_create(db: Session, author: AuthorCreate, file):
    model = Author(**author.dict())
    file_path = os.path.join("img", author.img_name)  # Adjust path as per your requirement
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.read())
        db.add(model)
        db.commit()
        db.refresh(model)
        return model.__dict__
    except Exception as e:
        # Handle the exception appropriately
        print("Error occurred:", str(e))
        return None



def tag_create(db: Session, tag: TagCreate):
    model = Tag(**tag.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return tag.__dict__



def cat_create(db: Session, cat: CatCreate):
    model = Category(**cat.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return cat.__dict__



def comment_create(db: Session, comment: CommentCreate):
    model = Comment(**comment.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return comment.__dict__