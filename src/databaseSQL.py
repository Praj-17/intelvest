from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///src/portfolio.db',connect_args={"check_same_thread":False}) 

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()