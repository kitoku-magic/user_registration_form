from src.model import *
from src.model.generate import *

class pre_users_base(timestamp_mixin, model):
    __abstract__ = True
    __MAIL_ADDRESS_LENGTH = 512
    __TOKEN_LENGTH = 128

    def get_mail_address_length(cls):
        return pre_users_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls):
        return pre_users_base.__TOKEN_LENGTH

    @declared_attr
    def pre_user_id(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(pre_users_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls):
        return model.get_db_instance(model).Column(VARBINARY(pre_users_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')

    def __init__(self):
        model.__init__(self)
