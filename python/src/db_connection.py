from src.database import db

class db_connection:
    """
    DBのコネクションを保持するクラス（シングルトンを想定）
    """
    __instance = None
    def __new__(cls, *args, **kwargs):
        """
        クラスインスタンス生成前に、既にインスタンスが生成済みか確認してシングルトンを保証する
        """
        if cls.__instance is None:
            cls.__instance = super(db_connection, cls).__new__(cls)
            cls.__instance.__connection = db.engine.raw_connection()
        return cls.__instance
    def get_connection(self):
        return self.__connection
