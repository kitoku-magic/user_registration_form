from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class birth_days_entity_base(timestamp_mixin_entity, entity):
    """
    誕生日マスタテーブルエンティティの基底クラス
    """
    __abstract__ = True

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
    def set_validation_setting(self):
        pass
    def get_update_column_name_list(self):
        return ['birth_day']
