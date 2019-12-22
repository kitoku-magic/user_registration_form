from src.model import *
from src.model.generate import *

class prefectures_base(timestamp_mixin, model):
    __abstract__ = True
    prefecture_name_length = 12

    @declared_attr
    def prefecture_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '都道府県ID')
    @declared_attr
    def prefecture_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(prefectures_base.prefecture_name_length), nullable = False, server_default = '', comment = '都道府県名')
    @declared_attr
    def users_collection(cls):
        return model.get_db_instance(model).relationship('users', back_populates='prefectures', cascade='save-update, merge, delete', uselist=True)
    @declared_attr
    def zip_addresses_collection(cls):
        return model.get_db_instance(model).relationship('zip_addresses', back_populates='prefectures', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
