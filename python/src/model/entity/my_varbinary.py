from src.model.entity import setting, TypeDecorator, VARBINARY

class my_varbinary(TypeDecorator):
    """
    VARBINARYを拡張した独自型（sqlalchemy/sql/sqltypes.py の944行目のstrからbytesへのキャストでエラーになる為）
    """
    impl = VARBINARY

    def bind_processor(self, dialect):
        if dialect.dbapi is None:
            return None

        DBAPIBinary = dialect.dbapi.Binary

        def process(value):
            # bytes型が入って来るケースは無い？
            if isinstance(value, bytes):
                return value.decode(setting.app.config['PG_CHARACTER_SET'])
            else:
                return value

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            result = ''
            # bytes型が入って来るケースは無い？
            if isinstance(value, bytes):
                result = value.decode(setting.app.config['PG_CHARACTER_SET'])
            else:
                result = value
            return result
        return process
