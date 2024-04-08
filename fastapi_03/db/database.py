from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DB_URL = 'sqlite:///./books.db'

engine = create_engine(url=DB_URL)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
