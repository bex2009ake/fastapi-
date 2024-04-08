from sqlalchemy import Column, Integer, String, ForeignKey, Table, LargeBinary
from db.database import Base
from sqlalchemy.orm import relationship



post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post', Integer, ForeignKey('post.id')),
    Column('tag', Integer, ForeignKey('tag.id'))
)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, unique=True, nullable=False)

    posts = relationship('Post', secondary=post_tags, back_populates='tags')


class Category(Base):
    __tablename__ = 'category'

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, unique=True)

    posts = relationship('Post', back_populates='category')


class Author(Base):
    __tablename__ = 'author'

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String, unique=True, nullable=False)
    desc = Column('desc', String, nullable=False)
    img_name = Column('img_name', String, nullable=False, unique=True)
    img = Column('img', LargeBinary, nullable=False)

    posts = relationship('Post', back_populates='author', cascade='all, delete')


class Comment(Base):
    __tablename__ = 'comment'

    id = Column('id', Integer, primary_key=True, index=True)
    user_name = Column('username', String, nullable=False)
    msg = Column('msg', String, nullable=False)

    posts = relationship('Post', back_populates='comments')
    post_id = Column('post_id', Integer, ForeignKey('post.id'))




class Post(Base):
    __tablename__ = 'post'

    id = Column('id', Integer, primary_key=True, index=True)
    title = Column('title', String, nullable=False)
    desc = Column('desc', String, nullable=False)
    img_name = Column('img_name', String, nullable=False, unique=True)
    img = Column('img', LargeBinary, nullable=False)


    author_id = Column('author_id', Integer, ForeignKey('author.id'))
    cat_id = Column('cat_id', Integer, ForeignKey('category.id'))



    author = relationship('Author', back_populates='posts')
    category = relationship('Category', back_populates='posts')
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')
    comments = relationship('Comment', back_populates='posts', cascade='all, delete')