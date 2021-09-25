from python_library.src.custom_sqlalchemy.repository import repository
from src import typing
from src.model.entity.contact_methods_entity import contact_methods_entity

T = typing.TypeVar('T', bound='contact_methods_repository')

class contact_methods_repository(repository):
    """
    連絡方法マスタテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], contact_methods_entity: contact_methods_entity) -> None:
        super().__init__(contact_methods_entity)
