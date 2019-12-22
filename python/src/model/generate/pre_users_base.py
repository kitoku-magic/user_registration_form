from src.model import *
from src.model.generate import *

class pre_users_base(timestamp_mixin, model):
    __abstract__ = True
    mail_address_length = 512
    token_length = 128

    @declared_attr
    def pre_user_id(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(pre_users_base.mail_address_length), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls):
        return model.get_db_instance(model).Column(VARBINARY(pre_users_base.token_length), nullable = False, server_default = '', comment = 'トークン値')
    def __init__(self):
        model.__init__(self)
