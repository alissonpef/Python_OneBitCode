from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# postgresql://usuario:senha@host/database
# DATABASE_URI = "postgresql://postgresql:qwe12345@localhost/blog"
user = "postgres"
password = "qwe12345"
host = "localhost"
database = "blog"

DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
