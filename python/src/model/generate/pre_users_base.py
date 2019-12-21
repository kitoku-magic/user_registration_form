from src.model import *

class pre_users_base(timestamp_mixin, model):
    __tablename__ = 'pre_users'
    mail_address_length = 512
    token_length = 128
    pre_user_id = model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    mail_address = model.get_db_instance(model).Column(VARBINARY(mail_address_length), nullable = False, server_default = '', comment = 'メールアドレス')
    token = model.get_db_instance(model).Column(VARBINARY(token_length), nullable = False, server_default = '', comment = 'トークン値')

    def __init__(self):
        model.__init__(self)
