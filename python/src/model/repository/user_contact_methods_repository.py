from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.user_contact_methods_entity import user_contact_methods_entity

T = typing.TypeVar('T', bound='user_contact_methods_repository')

class user_contact_methods_repository(repository):
    """
    ユーザー連絡方法テーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], user_contact_methods_entity: user_contact_methods_entity) -> None:
        super().__init__(user_contact_methods_entity)
