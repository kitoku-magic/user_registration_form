from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class pre_users_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __MAIL_ADDRESS_LENGTH = 512
    __TOKEN_LENGTH = 128

    def get_mail_address_length(cls):
        return pre_users_entity_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls):
        return pre_users_entity_base.__TOKEN_LENGTH

    @declared_attr
    def pre_user_id(cls):
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(pre_users_entity_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(pre_users_entity_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
    def get_update_column_name_list(self):
        return ['mail_address', 'token']
