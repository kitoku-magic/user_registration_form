from src.model import *

class knew_triggers_base(timestamp_mixin, model):
    __tablename__ = 'knew_triggers'
    knew_trigger_name_length = 64
    knew_trigger_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '知ったきっかけID')
    knew_trigger_name = model.get_db_instance(model).Column(VARBINARY(knew_trigger_name_length), nullable = False, server_default = '', comment = '知ったきっかけ名')

    user_knew_triggers_collection = model.get_db_instance(model).relationship('user_knew_triggers_base', back_populates='knew_triggers', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
