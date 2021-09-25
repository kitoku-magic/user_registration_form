from src import typing
from src.model.entity.generate.contact_methods_entity_base import contact_methods_entity_base

T = typing.TypeVar('T', bound='contact_methods_entity')

class contact_methods_entity(contact_methods_entity_base):
    """
    連絡方法マスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
