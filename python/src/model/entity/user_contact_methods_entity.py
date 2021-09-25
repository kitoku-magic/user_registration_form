from src import typing
from src.model.entity.generate.user_contact_methods_entity_base import user_contact_methods_entity_base

T = typing.TypeVar('T', bound='user_contact_methods_entity')

class user_contact_methods_entity(user_contact_methods_entity_base):
    """
    ユーザー連絡方法テーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
