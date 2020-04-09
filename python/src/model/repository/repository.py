import math
import time
from src.database import db
from src.db_connection import db_connection
from src.model.repository import *

class repository():
    """
    全てのテーブルの基底リポジトリクラス
    """
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
    def get_main_entity(self):
        return self.__main_entity
    def select(self, columns, where = '', params = (), order_by = '', for_update = False):
        """
        SELECT文を実行する
        """
        # TODO: GROUP BYなど足りない分は、必要に応じて追加
        sql = 'SELECT ' + ', '.join(columns)
        if self.__table_name is not None:
            sql += ' FROM ' + self.__table_name
        if '' != where:
            sql += ' WHERE ' + where
        if '' != order_by:
            sql += ' ORDER BY ' + order_by
        if True == for_update:
            sql += ' FOR UPDATE'
        self.__cursor.execute(sql, params)
    def find(self, columns, where = '', params = (), order_by = '', for_update = False):
        """
        該当するデータを１件取得する
        """
        self.select(columns, where, params, order_by, for_update)
        return self.__cursor.fetchone()
        #query = self.get_db_instance().session.query(select)
        #if 0 < len(params):
        #    query = query.filter(text(where)).params(params)
        #return query.all()
    def find_all(self, columns, where = '', params = (), order_by = ''):
        """
        該当するデータを全件取得する
        """
        self.select(columns, where, params, order_by)
        return self.__cursor.fetchall()
    def insert(self, columns):
        """
        INSERT文を実行する
        """
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
    def bulk_insert(self, entities):
        """
        BULK INSERT文を実行する
        """
        sql = 'INSERT INTO '
        table_name = ''
        column_names = ''
        values = ''
        bind_values = list()
        for entity in entities:
            self.__main_entity = entity
            table_name = self.__main_entity.__tablename__
            columns = self.set_timestamp('ins', self.__main_entity.get_update_column_name_list())
            tmp_column_names = ''
            tmp_values = ''
            for column in columns:
                tmp_column_names += column + ', '
                tmp_values += '%s, '
                bind_values.append(getattr(self.__main_entity, column))
            column_names = tmp_column_names
            values += '(' + tmp_values.rstrip(', ') + '),'
        sql += table_name + '('
        column_names = column_names.rstrip(', ')
        values = values.rstrip(',')
        sql += column_names + ') VALUES' + values + ';'
        return self.execute_update(sql, bind_values)
    def update(self, columns, where = '', params = ()):
        """
        UPDATE文を実行する
        """
        columns = self.set_timestamp('upd', columns)
        sql = 'UPDATE ' + self.__table_name + ' SET '
        bind_values = list()
        for column in columns:
            sql += column + ' = %s, '
            bind_values.append(getattr(self.__main_entity, column))
        sql = sql.rstrip(', ')
        if '' != where:
            sql += ' WHERE ' + where
            for value in params:
                bind_values.append(value)
        return self.execute_update(sql, bind_values)
    def delete(self, where = '', params = ()):
        """
        DELETE文を実行する
        """
        sql = 'DELETE FROM ' + self.__table_name
        bind_values = list()
        if '' != where:
            sql += ' WHERE ' + where
            for value in params:
                bind_values.append(value)
        return self.execute_update(sql, bind_values)
    def set_timestamp(self, mode, columns):
        """
        タイムスタンプ値を設定する
        """
        self_dict = self.__main_entity.__dict__
        if 'ins' == mode:
            if 'created_at' in self_dict:
                self.__main_entity.created_at = math.floor(time.time())
                columns.append('created_at')
        if 'updated_at' in self_dict:
            self.__main_entity.updated_at = math.floor(time.time())
            columns.append('updated_at')
        return columns
    def execute_update(self, sql, bind_values):
        """
        データを追加・更新・削除する
        """
        self.__cursor.execute(sql, tuple(bind_values))
        return self.__cursor.rowcount
    def last_insert_id(self):
        """
        直近の主キーの値を取得
        """
        return self.__cursor.lastrowid
    def begin(self, consistent_snapshot=False, isolation_level=None, readonly=None):
        """
        トランザクション開始
        """
        self.__db_connection.start_transaction(consistent_snapshot, isolation_level, readonly)
    def commit(self):
        """
        トランザクションコミット
        """
        self.__db_connection.commit()
        #self.get_db_instance().session.commit()
    def rollback(self):
        """
        トランザクションロールバック
        """
        self.__db_connection.rollback()
        #self.get_db_instance().session.rollback()
