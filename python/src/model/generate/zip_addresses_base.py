from src.model import *

class zip_addresses_base(timestamp_mixin, model):
    __tablename__ = 'zip_addresses'
    zip_code_length = 7
    city_district_county_length = 64
    town_village_address_length = 128
    zip_address_id = model.get_db_instance(model).Column(MEDIUMINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '郵便番号住所ID')
    zip_code = model.get_db_instance(model).Column(VARBINARY(zip_code_length), nullable = False, server_default = '', comment = '郵便番号')
    prefecture_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    city_district_county = model.get_db_instance(model).Column(VARBINARY(city_district_county_length), nullable = False, server_default = '', comment = '市区群')
    town_village_address = model.get_db_instance(model).Column(VARBINARY(town_village_address_length), nullable = False, server_default = '', comment = '町村番地')

    prefectures = model.get_db_instance(model).relationship('prefectures_base', back_populates='zip_addresses_collection', uselist=False)
    def __init__(self):
        model.__init__(self)
