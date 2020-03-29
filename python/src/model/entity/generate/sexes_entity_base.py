from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class sexes_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __SEX_NAME_LENGTH = 32

    def get_sex_name_length(cls):
        return sexes_entity_base.__SEX_NAME_LENGTH

    @declared_attr
    def sex_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '性別ID')
    @declared_attr
    def sex_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(sexes_entity_base.__SEX_NAME_LENGTH), nullable = False, server_default = '', comment = '性別名')
    @declared_attr
    def users_collection(cls):
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='sexes', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
    def get_update_column_name_list(self):
        return ['sex_name']
