from data.session_factory import create_session, get_session
from models.storage import Storage


# def get_storage_list():
#     session = create_session()
#
#     query = session.query(Storage).all()
#
#     storage_list = list(query)
#
#     session.close()
#
#     return storage_list

def get_storage_list(session):
    query = session.query(Storage).all()
    storage_list = list(query)

    return storage_list


def get_storage_title_by_id(storage_id, session):

    query = session.query(Storage).filter_by(id=storage_id).first()

    return query.title