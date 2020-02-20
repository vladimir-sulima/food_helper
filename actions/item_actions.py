from data.session_factory import create_session
from models.storage import Storage
from models.item import Item


def get_items_by_storage_id(id, session):
    query = session.query(Item).filter_by(storage_id=id).all()

    items_list = list(query)

    return items_list
