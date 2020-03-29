from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class prefectures_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __PREFECTURE_NAME_LENGTH = 12

    def get_prefecture_name_length(cls):
        return prefectures_entity_base.__PREFECTURE_NAME_LENGTH

    @declared_attr
    def prefecture_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '都道府県ID')
    @declared_attr
    def prefecture_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(prefectures_entity_base.__PREFECTURE_NAME_LENGTH), nullable = False, server_default = '', comment = '都道府県名')
    @declared_attr
    def zip_addresses_collection(cls):
        return repository.get_db_instance(repository).relationship('zip_addresses_entity', back_populates='prefectures', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
    def get_update_column_name_list(self):
        return ['prefecture_name']
