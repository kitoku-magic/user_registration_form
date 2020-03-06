from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class zip_addresses_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __ZIP_CODE_LENGTH = 7
    __CITY_DISTRICT_COUNTY_LENGTH = 64
    __TOWN_VILLAGE_ADDRESS_LENGTH = 128

    def get_zip_code_length(cls):
        return zip_addresses_entity_base.__ZIP_CODE_LENGTH
    def get_city_district_county_length(cls):
        return zip_addresses_entity_base.__CITY_DISTRICT_COUNTY_LENGTH
    def get_town_village_address_length(cls):
        return zip_addresses_entity_base.__TOWN_VILLAGE_ADDRESS_LENGTH

    @declared_attr
    def zip_address_id(cls):
        return repository.get_db_instance(repository).Column(MEDIUMINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '郵便番号住所ID')
    @declared_attr
    def zip_code(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(zip_addresses_entity_base.__ZIP_CODE_LENGTH), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_district_county(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(zip_addresses_entity_base.__CITY_DISTRICT_COUNTY_LENGTH), nullable = False, server_default = '', comment = '市区群')
    @declared_attr
    def town_village_address(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(zip_addresses_entity_base.__TOWN_VILLAGE_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '町村番地')
    @declared_attr
    def prefectures(cls):
        return repository.get_db_instance(repository).relationship('prefectures_entity', back_populates='zip_addresses_collection', uselist=False)
    @declared_attr
    def users_collection(cls):
        return repository.get_db_instance(repository).relationship('users_entity', primaryjoin='and_(zip_addresses_entity.zip_code == users_entity.zip_code, zip_addresses_entity.prefecture_id == users_entity.prefecture_id)', back_populates='zip_addresses', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
