from src.model.repository import *

class users_repository(repository):
    def __init__(self, users_entity):
        super().__init__(users_entity)
#    __db_instance = db
#    def __init__(self):
#        self.__validate_errors = {'result': True, 'error': []}
#        self.__db_connection = self.__db_instance.engine.raw_connection()
#        self.__cursor = self.__db_connection.cursor(prepared=True)
#    def get_db_instance(self):
#        return self.__db_instance
#    def get_db_connection(self):
#        return self.__db_connection
#    def get_cursor(self):
#        return self.__cursor
#    def get_validate_errors(self):
#        return self.__validate_errors
#    def select(self, columns, table_name = '', where = '', params = ()):
#        sql = 'SELECT ' + ', '.join(columns)
#        if table_name != '':
#            sql += ' FROM ' + table_name
#        if where != '':
#            sql += ' WHERE ' + where
#        self.__cursor.execute(sql, params)
#    def find(self, columns, table_name = '', where = '', params = ()):
#        self.select(columns, table_name, where, params)
#        return self.__cursor.fetchone()
#        #query = self.get_db_instance().session.query(select)
#        #if 0 < len(params):
#        #    query = query.filter(text(where)).params(params)
#        #return query.all()
#    def find_all(self, columns, table_name = '', where = '', params = ()):
#        self.select(columns, table_name, where, params)
#        return self.__cursor.fetchall()
#    def insert(self, columns):
#        columns = self.set_timestamp('ins', columns)
#        sql = 'INSERT INTO ' + self.__tablename__ + '('
#        values = ''
#        bind_values = list()
#        for column in columns:
#            sql += column + ', '
#            values += '%s, '
#            bind_values.append(getattr(self, column))
#        sql = sql.rstrip(', ')
#        values = values.rstrip(', ')
#        sql += ') VALUES(' + values + ');'
#        return self.execute_update(sql, bind_values)
#        #self.get_db_instance().session.add_all(insert_data)
#        #insert_list = list()
#        #for d in insert_data:
#            #insert_list.append(d.__dict__)
#        #self.get_db_instance().session.execute(table.__table__.insert(), insert_list)
#    def update(self, columns, where = '', params = ()):
#        columns = self.set_timestamp('upd', columns)
#        sql = 'UPDATE ' + self.__tablename__ + ' SET '
#        bind_values = list()
#        for column in columns:
#            sql += column + ' = %s, '
#            bind_values.append(getattr(self, column))
#        sql = sql.rstrip(', ')
#        if where != '':
#            sql += ' WHERE ' + where
#            for value in params:
#                bind_values.append(value)
#        return self.execute_update(sql, bind_values)
#    def set_timestamp(self, mode, columns):
#        self_dict = self.__dict__
#        if mode == 'ins':
#            if 'created_at' in self_dict:
#                self.created_at = math.floor(time.time())
#                columns.append('created_at')
#        if 'updated_at' in self_dict:
#            self.updated_at = math.floor(time.time())
#            columns.append('updated_at')
#        return columns
#    def execute_update(self, sql, bind_values):
#        self.__cursor.execute(sql, tuple(bind_values))
#        return self.__cursor.rowcount
#    def last_insert_id(self):
#        return self.__cursor.lastrowid
#    def begin(self, consistent_snapshot=False, isolation_level=None, readonly=None):
#        self.__db_connection.start_transaction(consistent_snapshot, isolation_level, readonly)
#    def commit(self):
#        self.__db_connection.commit()
#        #self.get_db_instance().session.commit()
#    def rollback(self):
#        self.__db_connection.rollback()
#        #self.get_db_instance().session.rollback()
