from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.user_knew_triggers_entity import user_knew_triggers_entity

T = typing.TypeVar('T', bound='user_knew_triggers_repository')

class user_knew_triggers_repository(repository):
    """
    ユーザー知ったきっかけテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], user_knew_triggers_entity: user_knew_triggers_entity) -> None:
        super().__init__(user_knew_triggers_entity)
