from src import typing
from src.model.entity.generate.jobs_entity_base import jobs_entity_base

T = typing.TypeVar('T', bound='jobs_entity')

class jobs_entity(jobs_entity_base):
    """
    職業マスタテーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
