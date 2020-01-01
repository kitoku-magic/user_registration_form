from src.model import *
from src.model.generate import *

class zip_addresses_base(timestamp_mixin, model):
    __abstract__ = True
    __ZIP_CODE_LENGTH = 7
    __CITY_DISTRICT_COUNTY_LENGTH = 64
    __TOWN_VILLAGE_ADDRESS_LENGTH = 128

    def get_zip_code_length(cls):
        return zip_addresses_base.__ZIP_CODE_LENGTH
    def get_city_district_county_length(cls):
        return zip_addresses_base.__CITY_DISTRICT_COUNTY_LENGTH
    def get_town_village_address_length(cls):
        return zip_addresses_base.__TOWN_VILLAGE_ADDRESS_LENGTH

    @declared_attr
    def zip_address_id(cls):
        return model.get_db_instance(model).Column(MEDIUMINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '郵便番号住所ID')
    @declared_attr
    def zip_code(cls):
        return model.get_db_instance(model).Column(VARBINARY(zip_addresses_base.__ZIP_CODE_LENGTH), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_district_county(cls):
        return model.get_db_instance(model).Column(VARBINARY(zip_addresses_base.__CITY_DISTRICT_COUNTY_LENGTH), nullable = False, server_default = '', comment = '市区群')
    @declared_attr
    def town_village_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(zip_addresses_base.__TOWN_VILLAGE_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '町村番地')
    @declared_attr
    def prefectures(cls):
        return model.get_db_instance(model).relationship('prefectures', back_populates='zip_addresses_collection', uselist=False)

    def __init__(self):
        model.__init__(self)
