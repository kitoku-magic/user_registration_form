from src.database import db
from src.model import *

class model(db.Model):
    __abstract__ = True
    __db_instance = db
    def __init__(self):
        self.__validate_errors = {'result': True, 'error': []}
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    def get_db_instance(self):
        return self.__db_instance
    def get_validate_errors(self):
        return self.__validate_errors
    def set_request_to_model(self, require_params, request_data):
        for k, v in require_params.items():
            value = request_data.get(k)
            if value is None:
                setattr(self, k, v)
            else:
                setattr(self, k, value)
    def find(self, select, where, params):
        query = self.get_db_instance().session.query(select)
        if 0 < len(params):
            query = query.filter(text(where)).params(params)
        return query.all()
    def insert(self, insert_data):
        self.get_db_instance().session.add_all(insert_data)
        self.get_db_instance().session.flush()
    def commit(self):
        self.get_db_instance().session.commit()
    def rollback(self):
        self.get_db_instance().session.rollback()
