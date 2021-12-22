from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    age = Column(Integer)
    email = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)


class SessionLogging(Base):
    __tablename__ = "SessionLogin"

    id = Column(Integer, primary_key=True, index=True)
    hashLogin = Column(String)