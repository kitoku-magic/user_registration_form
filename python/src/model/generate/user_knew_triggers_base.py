from src.model import *
from src.model.generate import *

class user_knew_triggers_base(timestamp_mixin, model):
    __abstract__ = True

    @declared_attr
    def user_id(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), model.get_db_instance(model).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def knew_trigger_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('knew_triggers.knew_trigger_id'), nullable = False, server_default = '0', primary_key = True, comment = '知ったきっかけID')
    @declared_attr
    def knew_triggers(cls):
        return model.get_db_instance(model).relationship('knew_triggers', back_populates='user_knew_triggers_collection', uselist=False)
    @declared_attr
    def users(cls):
        return model.get_db_instance(model).relationship('users', back_populates='user_knew_triggers_collection', uselist=False)

    def __init__(self):
        model.__init__(self)
