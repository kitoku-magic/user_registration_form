from src import typing
from src.model.entity.generate.birth_days_entity_base import birth_days_entity_base

T = typing.TypeVar('T', bound='birth_days_entity')

class birth_days_entity(birth_days_entity_base):
    """
    誕生日マスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
