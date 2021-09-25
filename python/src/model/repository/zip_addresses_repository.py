from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.zip_addresses_entity import zip_addresses_entity

T = typing.TypeVar('T', bound='zip_addresses_repository')

class zip_addresses_repository(repository):
    """
    郵便番号住所マスタテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], zip_addresses_entity: zip_addresses_entity) -> None:
        super().__init__(zip_addresses_entity)
