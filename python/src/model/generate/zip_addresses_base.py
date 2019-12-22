from src.model import *
from src.model.generate import *

class zip_addresses_base(timestamp_mixin, model):
    __abstract__ = True
    zip_code_length = 7
    city_district_county_length = 64
    town_village_address_length = 128

    @declared_attr
    def zip_address_id(cls):
        return model.get_db_instance(model).Column(MEDIUMINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '郵便番号住所ID')
    @declared_attr
    def zip_code(cls):
        return model.get_db_instance(model).Column(VARBINARY(zip_addresses_base.zip_code_length), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_district_county(cls):
        return model.get_db_instance(model).Column(VARBINARY(zip_addresses_base.city_district_county_length), nullable = False, server_default = '', comment = '市区群')
    @declared_attr
    def town_village_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(zip_addresses_base.town_village_address_length), nullable = False, server_default = '', comment = '町村番地')
    @declared_attr
    def prefectures(cls):
        return model.get_db_instance(model).relationship('prefectures', back_populates='zip_addresses_collection', uselist=False)
    def __init__(self):
        model.__init__(self)
