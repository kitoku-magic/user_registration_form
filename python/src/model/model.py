import time
import math

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
    def insert_raw(self, obj, columns):
        #self.get_db_instance().session.add_all(insert_data)
        #insert_list = list()
        #for d in insert_data:
            #insert_list.append(d.__dict__)
        #self.get_db_instance().session.execute(table.__table__.insert(), insert_list)
        obj_dict = obj.__dict__
        if 'created_at' in obj_dict:
            obj.created_at = math.floor(time.time())
            columns.append('created_at')
        if 'updated_at' in obj_dict:
            obj.updated_at = math.floor(time.time())
            columns.append('updated_at')
        sql = 'INSERT INTO ' + obj.__tablename__ + '('
        values = ''
        bind_values = {}
        for column in columns:
            sql += column + ', '
            values += ':' + column + ', '
            bind_values[column] = getattr(obj, column)
        sql = sql.rstrip(', ')
        values = values.rstrip(', ')
        sql += ') VALUES(' + values + ');'
        self.get_db_instance().session.execute(sql, bind_values)
        self.get_db_instance().session.flush()
    def begin(self):
        self.get_db_instance().session.begin(subtransactions=True)
    def commit(self):
        self.get_db_instance().session.commit()
    def rollback(self):
        self.get_db_instance().session.rollback()
