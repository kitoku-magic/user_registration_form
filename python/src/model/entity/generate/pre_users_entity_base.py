from src.database import db
from src.model.entity import declared_attr, entity, BIGINT, my_varbinary, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar

T = TypeVar('T', bound='pre_users_entity_base')

class pre_users_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー事前登録情報テーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __MAIL_ADDRESS_LENGTH: int = 512
    __TOKEN_LENGTH: int = 128

    def get_mail_address_length(cls: Type[T]) -> int:
        return pre_users_entity_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls: Type[T]) -> int:
        return pre_users_entity_base.__TOKEN_LENGTH

    @declared_attr
    def pre_user_id(cls: Type[T]) -> Column:
        return db.Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(pre_users_entity_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(pre_users_entity_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: Type[T]) -> List[str]:
        return ['mail_address', 'token', 'created_at', 'updated_at']
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['mail_address', 'token', 'updated_at']
