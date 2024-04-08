from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Books(Base):
    __tablename__ = 'Books'


    id = Column('id', Integer, primary_key=True, index=True)
    title = Column('title', String, nullable=False)
    author = Column('author', String, nullable=False)
    price = Column('price', Integer, nullable=False)


class Tags(Base):
    __tablename__ = 'Tag'


    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, nullable=False)


class Categorys(Base):
    __tablename__ = 'Category'


    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, nullable=False)


class Authors(Base):
    __tablename__ = 'Author'


    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
