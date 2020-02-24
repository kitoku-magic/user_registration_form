from src.database import db

class db_connection:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(db_connection, cls).__new__(cls)
            cls.__instance.__connection = db.engine.raw_connection()
        return cls.__instance
    def get_connection(self):
        return self.__connection
