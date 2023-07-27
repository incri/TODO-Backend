from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgres://todos_databse_user:ZEJE0K2hmPMo0VcXUk7OAZLfk3QQjAhw@dpg-cj12sj5ph6enmk775mjg-a.singapore-postgres.render.com/todos_databse"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
