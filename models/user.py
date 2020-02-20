import sys

from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from models.model_base import ModelBase
from helpers.db_connection_helper import access_db


class User(ModelBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    user_name = Column(String(25), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    created_date_utc = Column(DateTime(), default=datetime.utcnow)

