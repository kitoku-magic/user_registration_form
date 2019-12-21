from src.model import *

class prefectures_base(timestamp_mixin, model):
    __tablename__ = 'prefectures'
    prefecture_name_length = 12
    prefecture_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '都道府県ID')
    prefecture_name = model.get_db_instance(model).Column(VARBINARY(prefecture_name_length), nullable = False, server_default = '', comment = '都道府県名')

    zip_addresses_collection = model.get_db_instance(model).relationship('zip_addresses_base', back_populates='prefectures', cascade='save-update, merge, delete', uselist=True)
    users_collection = model.get_db_instance(model).relationship('users_base', back_populates='prefectures', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
