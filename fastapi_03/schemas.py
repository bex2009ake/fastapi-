from pydantic import BaseModel, Field, validator

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=212)
    author: str = Field(min_length=1, max_length=212)
    description: str = Field(min_length=1, max_length=212)
    price: int = Field(gt=0, lt=1000)


class Author(BaseModel):
    name: str = Field(min_length=1, max_length=212)


class Category(BaseModel):
    name: str = Field(min_length=1, max_length=212)


class Tag(BaseModel):
    name: str = Field(min_length=1, max_length=212)
