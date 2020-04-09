from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class user_knew_triggers_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー知ったきっかけテーブルエンティティの基底クラス
    """
    __abstract__ = True

    @declared_attr
    def user_id(cls):
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def knew_trigger_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('knew_triggers.knew_trigger_id'), nullable = False, server_default = '0', primary_key = True, comment = '知ったきっかけID')
    @declared_attr
    def knew_triggers(cls):
        return repository.get_db_instance(repository).relationship('knew_triggers_entity', back_populates='user_knew_triggers_collection', uselist=False)
    @declared_attr
    def users(cls):
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='user_knew_triggers_collection', uselist=False)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self):
        pass
    def get_update_column_name_list(self):
        return ['user_id', 'knew_trigger_id']
