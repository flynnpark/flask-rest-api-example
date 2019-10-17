from sqlalchemy import Column, Integer, String, Text
from werkzeug.security import generate_password_hash, check_password_hash
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), index=True, unique=True)
    name = Column(String(50))
    password = Column(String(128))
    bio = Column(Text())

    def __init__(self, email, name, password, bio=None):
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)
        self.bio = bio

    def check_password(self, password):
        return check_password_hash(self.password, password)
