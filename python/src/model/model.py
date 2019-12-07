import time
import math

from src.database import db
from src.model import *

class model(db.Model):
    __abstract__ = True
    __db_instance = db
    __db_connection = None
    __cursor = None
    __validate_errors = {}
    def __init__(self):
        self.__validate_errors = {'result': True, 'error': []}
        self.__db_connection = self.__db_instance.engine.raw_connection()
        self.__cursor = self.__db_connection.cursor(prepared=True)
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    def get_db_instance(self):
        return self.__db_instance
    def get_db_connection(self):
        return self.__db_connection
    def get_cursor(self):
        return self.__cursor
    def get_validate_errors(self):
        return self.__validate_errors
    def set_request_to_model(self, require_params, request_data):
        for k, v in require_params.items():
            value = request_data.get(k)
            if value is None:
                setattr(self, k, v)
            else:
                setattr(self, k, value)
    def select(self, columns, table_name = '', where = '', params = {}):
        sql = 'SELECT ' + ', '.join(columns)
        if table_name != '':
            sql += ' FROM ' + table_name
        if where != '':
            sql += ' WHERE ' + where
        self.__cursor.execute(sql, params)
    def find(self, columns, table_name = '', where = '', params = {}):
        self.select(columns, table_name, where, params)
        return self.__cursor.fetchone()
        #query = self.get_db_instance().session.query(select)
        #if 0 < len(params):
        #    query = query.filter(text(where)).params(params)
        #return query.all()
    def find_all(self, columns, table_name = '', where = '', params = {}):
        self.select(columns, table_name, where, params)
        return self.__cursor.fetchall()
    def insert(self, obj, columns):
        obj_dict = obj.__dict__
        if 'created_at' in obj_dict:
            obj.created_at = math.floor(time.time())
            columns.append('created_at')
        if 'updated_at' in obj_dict:
            obj.updated_at = math.floor(time.time())
            columns.append('updated_at')
        sql = 'INSERT INTO ' + obj.__tablename__ + '('
        values = ''
        bind_values = list()
        for column in columns:
            sql += column + ', '
            values += '%s, '
            bind_values.append(getattr(obj, column))
        sql = sql.rstrip(', ')
        values = values.rstrip(', ')
        sql += ') VALUES(' + values + ');'
        self.__cursor.execute(sql, tuple(bind_values))
        return self.__cursor.rowcount
        #self.get_db_instance().session.add_all(insert_data)
        #insert_list = list()
        #for d in insert_data:
            #insert_list.append(d.__dict__)
        #self.get_db_instance().session.execute(table.__table__.insert(), insert_list)
    def last_insert_id(self):
        return self.__cursor.lastrowid
    def begin(self, subtransactions = False):
        pass
        #self.__db_connection.begin()
        #self.get_db_instance().session.begin(subtransactions)
    def commit(self):
        self.__db_connection.commit()
        #self.get_db_instance().session.commit()
    def rollback(self):
        self.__db_connection.rollback()
        #self.get_db_instance().session.rollback()
