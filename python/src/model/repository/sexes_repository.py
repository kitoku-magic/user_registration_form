from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.sexes_entity import sexes_entity

T = typing.TypeVar('T', bound='sexes_repository')

class sexes_repository(repository):
    """
    性別マスタテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], sexes_entity: sexes_entity) -> None:
        super().__init__(sexes_entity)
