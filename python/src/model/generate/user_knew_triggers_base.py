from src.model import *

class user_knew_triggers_base(timestamp_mixin, model):
    __tablename__ = 'user_knew_triggers'
    user_id = model.get_db_instance(model).Column(BIGINT(unsigned = True), model.get_db_instance(model).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    knew_trigger_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('knew_triggers.knew_trigger_id'), nullable = False, server_default = '0', primary_key = True, comment = '知ったきっかけID')

    knew_triggers = model.get_db_instance(model).relationship('knew_triggers_base', back_populates='user_knew_triggers_collection', uselist=False)
    users = model.get_db_instance(model).relationship('users_base', back_populates='user_knew_triggers_collection', uselist=False)
    def __init__(self):
        model.__init__(self)
