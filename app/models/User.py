from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    name = Column(String(50))

    def __init__(self, name=None, email=None):
        self.email = email
        self.name = name
