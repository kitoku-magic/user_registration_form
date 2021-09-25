from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.pre_users_entity import pre_users_entity

T = typing.TypeVar('T', bound='pre_users_repository')

class pre_users_repository(repository):
    """
    ユーザー事前登録情報テーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], pre_users_entity: pre_users_entity) -> None:
        super().__init__(pre_users_entity)
