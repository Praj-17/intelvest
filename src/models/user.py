# app/models.py

from datetime import datetime, date
from sqlalchemy import (
    Column, Integer, String, Date, DateTime, Boolean, text, SmallInteger
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'tbl_user'

    user_Id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(255), nullable=True)
    mname = Column(String(255), nullable=True)
    lname = Column(String(255), nullable=True)
    dob = Column(Date, nullable=True)
    gender = Column(String(255), nullable=True)
    course = Column(String(255), nullable=True)
    yrlvl = Column(String(255), nullable=True)
    username = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    address = Column(String(250), nullable=True)
    phone = Column(String(50), nullable=True)
    eduboard = Column(String(200), nullable=True)
    email = Column(String(200), nullable=True)
    role_id = Column(Integer, nullable=False, default=3)
    state = Column(String(200), nullable=True)
    country = Column(String(200), nullable=True)
    pincode = Column(String(20), nullable=True)
    added_on = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    device_id = Column(String(50), nullable=False, default='test')
    isJMTUser = Column(Boolean, nullable=False, default=False)
    isActive = Column(SmallInteger, nullable=False, default=0)

    def __repr__(self):
        return f"<UserModel(user_Id={self.user_Id}, username='{self.username}', email='{self.email}')>"
