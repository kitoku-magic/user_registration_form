from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.prefectures_entity import prefectures_entity

T = typing.TypeVar('T', bound='prefectures_repository')

class prefectures_repository(repository):
    """
    都道府県マスタテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], prefectures_entity: prefectures_entity) -> None:
        super().__init__(prefectures_entity)
