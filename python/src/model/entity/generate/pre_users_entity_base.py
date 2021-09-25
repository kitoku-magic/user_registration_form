from src import typing
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sassc
from python_library.src.custom_sqlalchemy.custom_varbinary import custom_varbinary
from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='pre_users_entity_base')

class pre_users_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー事前登録情報テーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __MAIL_ADDRESS_LENGTH: int = 512
    __TOKEN_LENGTH: int = 128

    def get_mail_address_length(cls: typing.Type[T]) -> int:
        return pre_users_entity_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls: typing.Type[T]) -> int:
        return pre_users_entity_base.__TOKEN_LENGTH

    @saed.declared_attr
    def pre_user_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @saed.declared_attr
    def mail_address(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(pre_users_entity_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @saed.declared_attr
    def token(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(pre_users_entity_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['mail_address', 'token', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['mail_address', 'token', 'updated_at']
