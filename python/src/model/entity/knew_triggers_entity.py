from src import typing
from src.model.entity.generate.knew_triggers_entity_base import knew_triggers_entity_base

T = typing.TypeVar('T', bound='knew_triggers_entity')

class knew_triggers_entity(knew_triggers_entity_base):
    """
    知ったきっかけマスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
