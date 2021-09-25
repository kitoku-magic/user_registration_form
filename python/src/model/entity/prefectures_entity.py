from src import typing
from src.model.entity.generate.prefectures_entity_base import prefectures_entity_base

T = typing.TypeVar('T', bound='prefectures_entity')

class prefectures_entity(prefectures_entity_base):
    """
    都道府県マスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
