from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class knew_triggers_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __KNEW_TRIGGER_NAME_LENGTH = 64

    def get_knew_trigger_name_length(cls):
        return knew_triggers_entity_base.__KNEW_TRIGGER_NAME_LENGTH

    @declared_attr
    def knew_trigger_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '知ったきっかけID')
    @declared_attr
    def knew_trigger_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(knew_triggers_entity_base.__KNEW_TRIGGER_NAME_LENGTH), nullable = False, server_default = '', comment = '知ったきっかけ名')
    @declared_attr
    def user_knew_triggers_collection(cls):
        return repository.get_db_instance(repository).relationship('user_knew_triggers_entity', back_populates='knew_triggers', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
    def get_update_column_name_list(self):
        return ['knew_trigger_name']
