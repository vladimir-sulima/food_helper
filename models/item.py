import sys

from models.model_base import ModelBase
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Item(ModelBase):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(60), nullable=False)
    category = Column(String(30), nullable=False)
    measure = Column(String(15), nullable=False)
    amount = Column(Float, nullable=False)
    price = Column(Float, nullable=False, default=0)
    purchase = Column(DateTime, nullable=False)
    best_before_date = Column(DateTime, nullable=False)
    is_daily_product = Column(Boolean, nullable=False, default=False)
    is_frozen = Column(Boolean, nullable=False, default=False)

    storage_id = Column(Integer, ForeignKey("storage.id"), nullable=False)
    storage = relationship("Storage", back_populates="items")


#
# def show_items():
#     pass
#
#
# def add_item():
#     pass
#
#
# def remove_item():
#     pass
#
