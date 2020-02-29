from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class birth_days_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True

    def get_all_properties(self):
        return {
            'birth_day_id' : 0,
            'birth_day' : '0001-01-01',
            'created_at' : 0,
            'updated_at' : 0,
            'users_collection' : [],
        }

    @declared_attr
    def birth_day_id(cls):
        return repository.get_db_instance(repository).Column(SMALLINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '誕生日ID')
    @declared_attr
    def birth_day(cls):
        return repository.get_db_instance(repository).Column(DATE(), nullable = False, server_default = '0001-01-01', comment = '誕生日')
    @declared_attr
    def users_collection(cls):
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='birth_days', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
