from src import typing
from src.model.entity.generate.user_knew_triggers_entity_base import user_knew_triggers_entity_base

T = typing.TypeVar('T', bound='user_knew_triggers_entity')

class user_knew_triggers_entity(user_knew_triggers_entity_base):
    """
    ユーザー知ったきっかけテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
