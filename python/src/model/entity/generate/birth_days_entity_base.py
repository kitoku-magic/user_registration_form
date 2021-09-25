from src import typing
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc
from python_library.src import sasst

from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='birth_days_entity_base')

class birth_days_entity_base(timestamp_mixin_entity, entity):
    """
    誕生日マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True

    @saed.declared_attr
    def birth_day_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.SMALLINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '誕生日ID')
    @saed.declared_attr
    def birth_day(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sasst.DATE(), nullable = False, server_default = '0001-01-01', comment = '誕生日')
    @saed.declared_attr
    def users_collection(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('users_entity', back_populates='birth_days', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['birth_day', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['birth_day', 'updated_at']
