from src import typing
from src.model.entity.generate.sexes_entity_base import sexes_entity_base

T = typing.TypeVar('T', bound='sexes_entity')

class sexes_entity(sexes_entity_base):
    """
    性別マスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
