from src import typing
from src.model.entity.generate.zip_addresses_entity_base import zip_addresses_entity_base

T = typing.TypeVar('T', bound='zip_addresses_entity')

class zip_addresses_entity(zip_addresses_entity_base):
    """
    郵便番号住所マスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
