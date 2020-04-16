import math
import time
from src.db_manager import db_manager
from src.model.repository import *

class repository():
    """
    全てのテーブルの基底リポジトリクラス
    """
    __db_manager = None
    def __new__(cls, main_entity):
        cls.__db_manager = db_manager()
        return super().__new__(cls)
    def __init__(self, main_entity):
        self.__main_entity = main_entity
        self.__table_name = self.__main_entity.__tablename__
        self.__last_insert_id = None
    def get_db_manager(self):
        return self.__db_manager
    def get_main_entity(self):
        return self.__main_entity
    def select(self, columns, where = '', params = {}, order_by = '', for_update = False):
        """
        SELECT文を作成する
        """
        # TODO: GROUP BYなど足りない分は、必要に応じて追加
        query = self.get_db_manager().get_session().query(*columns)
        if 0 < len(params):
            query = query.filter(text(where)).params(**params)
        if '' != order_by:
            query = query.order_by(text(order_by))
        if True == for_update:
            query = query.with_for_update()
        return query
    def find(self, columns = (), where = '', params = {}, order_by = '', for_update = False):
        """
        該当するデータを１件取得する
        """
        return self.select(columns, where, params, order_by, for_update).first()
    def find_all(self, columns, where = '', params = (), order_by = ''):
        """
        該当するデータを全件取得する
        """
        return self.select(columns, where, params, order_by).all()
    def insert(self, insert_entity, auto_increment_column_name):
        """
        INSERT文を実行する
        """
        insert_entities = self.set_timestamp('ins', [insert_entity])
        self.get_db_manager().get_session().add(insert_entities[0])
        # flushする前に実行しないと、挿入件数が分からなくなるので、このタイミングで
        result = self.get_db_manager().get_session().new
        self.get_db_manager().get_session().flush()
        # flushすると、entityの内容が更新される
        self.__last_insert_id = getattr(insert_entities[0], auto_increment_column_name)
        return len(result)
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
    def update(self, table, columns, where = '', where_params = {}, synchronize_session = False):
        """
        UPDATE文を実行する
        """
        query = self.get_db_manager().get_session().query(table)
        if 0 < len(where_params):
            query = query.filter(text(where)).params(**where_params)
        columns = self.set_timestamp_raw('upd', columns)
        update_params = {}
        for column in columns:
            update_params[column] = getattr(self.__main_entity, column)
        row_count = query.update(update_params, synchronize_session = synchronize_session)
        return row_count
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
    def set_timestamp(self, mode, entities):
        """
        タイムスタンプ値を設定する
        """
        for entity in entities:
            if 'ins' == mode:
                if True == hasattr(entity, 'created_at'):
                    entity.created_at = math.floor(time.time())
            if True == hasattr(entity, 'updated_at'):
                entity.updated_at = math.floor(time.time())
        return entities
    def execute_update(self, sql, bind_values):
        """
        データを追加・更新・削除する
        """
        self.get_db_manager().get_cursor().execute(sql, tuple(bind_values))
        return self.get_db_manager().get_cursor().rowcount
    def last_insert_id(self):
        """
        直近の主キーの値を取得
        """
        return self.__last_insert_id
    def begin(self, subtransactions = True):
        """
        トランザクション開始
        """
        self.get_db_manager().get_session().begin(subtransactions)
    def commit(self):
        """
        トランザクションコミット
        """
        self.get_db_manager().get_session().commit()
    def rollback(self):
        """
        トランザクションロールバック
        """
        self.get_db_manager().get_session().rollback()
    # 以下は、ORM機能を用いないでSQLを実行する関数群
    def select_raw(self, columns, where = '', params = (), order_by = '', for_update = False):
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
        self.get_db_manager().get_cursor().execute(sql, params)
    def find_raw(self, columns, where = '', params = (), order_by = '', for_update = False):
        """
        該当するデータを１件取得する
        """
        self.select_raw(columns, where, params, order_by, for_update)
        return self.get_db_manager().get_cursor().fetchone()
    def find_all_raw(self, columns, where = '', params = (), order_by = ''):
        """
        該当するデータを全件取得する
        """
        self.select_raw(columns, where, params, order_by)
        return self.get_db_manager().get_cursor().fetchall()
    def insert_raw(self, columns):
        """
        INSERT文を実行する
        """
        columns = self.set_timestamp_raw('ins', columns)
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
        return self.execute_update_raw(sql, bind_values)
    def bulk_insert_raw(self, entities):
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
            columns = self.set_timestamp_raw('ins', self.__main_entity.get_update_column_name_list())
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
        return self.execute_update_raw(sql, bind_values)
    def update_raw(self, columns, where = '', params = ()):
        """
        UPDATE文を実行する
        """
        columns = self.set_timestamp_raw('upd', columns)
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
        return self.execute_update_raw(sql, bind_values)
    def delete_raw(self, where = '', params = ()):
        """
        DELETE文を実行する
        """
        sql = 'DELETE FROM ' + self.__table_name
        bind_values = list()
        if '' != where:
            sql += ' WHERE ' + where
            for value in params:
                bind_values.append(value)
        return self.execute_update_raw(sql, bind_values)
    def set_timestamp_raw(self, mode, columns):
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
    def execute_update_raw(self, sql, bind_values):
        """
        データを追加・更新・削除する
        """
        self.get_db_manager().get_cursor().execute(sql, tuple(bind_values))
        return self.get_db_manager().get_cursor().rowcount
    def last_insert_id_raw(self):
        """
        直近の主キーの値を取得
        """
        return self.get_db_manager().get_cursor().lastrowid
    def begin_raw(self, consistent_snapshot=False, isolation_level=None, readonly=None):
        """
        トランザクション開始
        """
        self.get_db_manager().get_connection().start_transaction(consistent_snapshot, isolation_level, readonly)
    def commit_raw(self):
        """
        トランザクションコミット
        """
        self.get_db_manager().get_connection().commit()
    def rollback_raw(self):
        """
        トランザクションロールバック
        """
        self.get_db_manager().get_connection().rollback()
