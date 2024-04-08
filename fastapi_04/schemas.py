from pydantic import BaseModel
from typing import List, Optional



class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True



class CatBase(BaseModel):
    name: str

class CatCreate(CatBase):
    pass

class Cat(CatBase):
    id: int

    class Config:
        from_attributes = True



class AuthorBase(BaseModel):
    name: str
    desc: str
    img_name: str
    img: bytes

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True



class CommentBase(BaseModel):
    user_name: str
    msg: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    class Config:
        from_attributes = True



class PostBase(BaseModel):
    title: str
    desc: str
    img_name: str
    img: bytes

class PostCreate(PostBase):
    author_id: int
    cat_id: int
    tags: List[int] = []

class Post(PostBase):
    id: int
    author: Author
    cat: Author
    tags: List[int] = []

    class Config:
        from_attributes = True

