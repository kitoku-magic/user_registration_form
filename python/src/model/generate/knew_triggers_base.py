from src.model import *
from src.model.generate import *

class knew_triggers_base(timestamp_mixin, model):
    __abstract__ = True
    __KNEW_TRIGGER_NAME_LENGTH = 64

    def get_knew_trigger_name_length(cls):
        return knew_triggers_base.__KNEW_TRIGGER_NAME_LENGTH

    @declared_attr
    def knew_trigger_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '知ったきっかけID')
    @declared_attr
    def knew_trigger_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(knew_triggers_base.__KNEW_TRIGGER_NAME_LENGTH), nullable = False, server_default = '', comment = '知ったきっかけ名')
    @declared_attr
    def user_knew_triggers_collection(cls):
        return model.get_db_instance(model).relationship('user_knew_triggers', back_populates='knew_triggers', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        model.__init__(self)
