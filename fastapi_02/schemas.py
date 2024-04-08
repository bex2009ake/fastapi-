from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime, date



class Tag(BaseModel):
    name: str = Field(..., max_length=100)


class Category(BaseModel):
    name: str = Field(..., max_length=100)


class Author(BaseModel):
    name: str = Field(..., max_length=200)
    email: str


    @validator('email')
    def check_email(cls, val):
        if not '@gmail.com' in val:
            raise ValueError('Incorrect email !!!')
        
        return val


class Post(BaseModel):
    id: int
    title: str = Field(..., max_length=300)
    content: str 
    author: Author
    category: Category
    tags: List[Tag]
    created_at: date = datetime.now