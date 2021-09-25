from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.birth_days_entity import birth_days_entity

T = typing.TypeVar('T', bound='birth_days_repository')

class birth_days_repository(repository):
    """
    誕生日マスタテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], birth_days_entity: birth_days_entity) -> None:
        super().__init__(birth_days_entity)
