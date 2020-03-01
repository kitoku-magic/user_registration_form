import time
import math

from src.database import db
from src.db_connection import db_connection
from src.model.repository import *

class repository():
    __db_instance = db
    __db_connection = None
    __cursor = None
    def __new__(cls, main_entity):
        db_connection_obj = db_connection()
        cls.__db_connection = db_connection_obj.get_connection()
        cls.__cursor = cls.__db_connection.cursor(prepared=True)
        return super().__new__(cls)
    def __init__(self, main_entity):
        self.__main_entity = main_entity
        self.__table_name = self.__main_entity.__tablename__
    def get_db_instance(cls):
        return cls.__db_instance
    def get_db_connection(cls):
        return cls.__db_connection
    def get_cursor(self):
        return self.__cursor
    def select(self, columns, where = '', params = (), order_by = '', for_update = False):
        sql = 'SELECT ' + ', '.join(columns)
        if self.__table_name is not None:
            sql += ' FROM ' + self.__table_name
        if where != '':
            sql += ' WHERE ' + where
        if order_by != '':
            sql += ' ORDER BY ' + order_by
        if for_update == True:
            sql += ' FOR UPDATE'
        self.__cursor.execute(sql, params)
    def find(self, columns, where = '', params = (), order_by = '', for_update = False):
        self.select(columns, where, params, order_by, for_update)
        return self.__cursor.fetchone()
        #query = self.get_db_instance().session.query(select)
        #if 0 < len(params):
        #    query = query.filter(text(where)).params(params)
        #return query.all()
    def find_all(self, columns, where = '', params = (), order_by = ''):
        self.select(columns, where, params, order_by)
        return self.__cursor.fetchall()
    def insert(self, columns):
        columns = self.set_timestamp('ins', columns)
        sql = 'INSERT INTO ' + self.__table_name + '('
        values = ''
        bind_values = list()
        for column in columns:
            sql += column + ', '
            values += '%s, '
            bind_values.append(getattr(self.__main_entity, column))
        sql = sql.rstrip(', ')
        values = values.rstrip(', ')
        sql += ') VALUES(' + values + ');'
        return self.execute_update(sql, bind_values)
        #self.get_db_instance().session.add_all(insert_data)
        #insert_list = list()
        #for d in insert_data:
            #insert_list.append(d.__dict__)
        #self.get_db_instance().session.execute(table.__table__.insert(), insert_list)
    def update(self, columns, where = '', params = ()):
        columns = self.set_timestamp('upd', columns)
        sql = 'UPDATE ' + self.__table_name + ' SET '
        bind_values = list()
        for column in columns:
            sql += column + ' = %s, '
            bind_values.append(getattr(self.__main_entity, column))
        sql = sql.rstrip(', ')
        if where != '':
            sql += ' WHERE ' + where
            for value in params:
                bind_values.append(value)
        return self.execute_update(sql, bind_values)
    def set_timestamp(self, mode, columns):
        self_dict = self.__main_entity.__dict__
        if mode == 'ins':
            if 'created_at' in self_dict:
                self.__main_entity.created_at = math.floor(time.time())
                columns.append('created_at')
        if 'updated_at' in self_dict:
            self.__main_entity.updated_at = math.floor(time.time())
            columns.append('updated_at')
        return columns
    def execute_update(self, sql, bind_values):
        self.__cursor.execute(sql, tuple(bind_values))
        return self.__cursor.rowcount
    def last_insert_id(self):
        return self.__cursor.lastrowid
    def begin(self, consistent_snapshot=False, isolation_level=None, readonly=None):
        self.__db_connection.start_transaction(consistent_snapshot, isolation_level, readonly)
    def commit(self):
        self.__db_connection.commit()
        #self.get_db_instance().session.commit()
    def rollback(self):
        self.__db_connection.rollback()
        #self.get_db_instance().session.rollback()
