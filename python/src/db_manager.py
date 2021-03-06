from src.database import db

class db_manager:
    """
    DB管理クラス（シングルトンを想定）
    """
    __instance = None
    def __new__(cls, *args, **kwargs):
        """
        クラスインスタンス生成前に、既にインスタンスが生成済みか確認してシングルトンを保証する
        """
        if cls.__instance is None:
            cls.__instance = super(db_manager, cls).__new__(cls)
            cls.__instance.__db_instance = db
            cls.__instance.__session = cls.__instance.__db_instance.session
        return cls.__instance
    def get_db_instance(self):
        return self.__db_instance
    def get_session(self):
        return self.__session
