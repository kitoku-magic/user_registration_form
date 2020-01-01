from src.model import *
from src.model.generate import *

class birth_days_base(timestamp_mixin, model):
    __abstract__ = True

    @declared_attr
    def birth_day_id(cls):
        return model.get_db_instance(model).Column(SMALLINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '誕生日ID')
    @declared_attr
    def birth_day(cls):
        return model.get_db_instance(model).Column(DATE(), nullable = False, server_default = '0001-01-01', comment = '誕生日')
    @declared_attr
    def users_collection(cls):
        return model.get_db_instance(model).relationship('users', back_populates='birth_days', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        model.__init__(self)
