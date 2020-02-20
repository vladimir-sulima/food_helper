import sys

from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models.model_base import ModelBase
from helpers.db_connection_helper import access_db


class Storage(ModelBase):
    __tablename__ = "storage"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)

    items = relationship("Item", back_populates="storage")



# def manage_storage():
#     while True:
#         selected_value = input("Select available option: ")
#
#         if selected_value == '1':
#             storage = get_all_storage()
#             show_all_storage(storage)
#         elif selected_value == "2":
#             add_storage()
#         elif selected_value == "3":
#             remove_storage()
#         elif selected_value == "4":
#             clear()
#             break
#         elif selected_value.lower() == "x":
#             sys.exit()
#         else:
#             print("Invalid option, please try again")


# def get_all_storage():
#     # storage_list = []
#     with access_db() as cursor:
#         cursor.execute("SELECT * FROM storage")
#
#         rows = cursor.fetchall()
#         # for storage in rows:
#         #     storage_list.append(storage)
#     return rows
# # def get_all_storage():
# #     storage_list = []
# #     with access_db() as cursor:
# #         cursor.execute("SELECT Name FROM storage")
# #
# #         rows = cursor.fetchall()
# #         for storage in rows:
# #             st = {'id': storage}
# #             storage_list.append(storage)
# #     return storage_list
#
#
# def show_all_storage(storage):
#     for st in storage:
#         print(st)
#
#
# def add_storage():
#     storage_name = input("Set storage name: ")
#
#     with access_db() as cursor:
#         # cursor.execute(f"INSERT INTO storage(title) VALUES('blahblah')")
#         sql = "INSERT INTO storage(title) VALUES(?)"
#         cursor.execute(sql, [storage_name])
#     print(f"Storage {storage_name} added successfully")
#
#
# def remove_storage():
#     pass