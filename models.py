from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String,create_engine

sql_url = "postgresql://postgres:admin@localhost/postgres"
engine = create_engine(sql_url)
session = sessionmaker(autocommit = False, autoflush= False, bind=engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

class ForPhone(Base):
    __tablename__ = "Madurai_mobiles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    modelName = Column(String, index=True)
    modelDescription = Column(String, index=True)
    price = Column(Integer, index=True)