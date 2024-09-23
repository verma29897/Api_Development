from sqlalchemy import Integer,Column,Boolean,String

from database import Base ,engine

def created_table():
    Base.metadata.create_all(engine)


class Person(Base):
    
    __tablename__ = 'person'
    
    id=Column(Integer,primary_key=True)
    first_name=Column(String,nullable=False)
    last_name=Column(String,nullable=False)
    isMale=Column(Boolean)
