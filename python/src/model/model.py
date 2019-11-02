from src.database import db

class model(db.Model):
    __abstract__ = True
    __db_instance = db
    def get_db_instance(self):
        return self.__db_instance
    def find_all(self, select):
        all_data = self.get_db_instance().session.query(select).all()
        return all_data
