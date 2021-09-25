from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.knew_triggers_entity import knew_triggers_entity

T = typing.TypeVar('T', bound='knew_triggers_repository')

class knew_triggers_repository(repository):
    """
    知ったきっかけマスタテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], knew_triggers_entity: knew_triggers_entity) -> None:
        super().__init__(knew_triggers_entity)
