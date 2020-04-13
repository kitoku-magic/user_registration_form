from sqlalchemy.dialects.mysql.mysqlconnector import MySQLExecutionContext_mysqlconnector

class custom_sql_execution_context(MySQLExecutionContext_mysqlconnector):
    """
    SQLの実行コンテキストクラス（静的プリペアドステートメントにする為にカスタマイズ）
    """
    def create_cursor(self):
        self._is_server_side = False
        return self._dbapi_connection.cursor(prepared=True)
