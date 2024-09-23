from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker



SQLALCHEMY_DATABASE_URL="postgresql://postgres:admin123@localhost:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
