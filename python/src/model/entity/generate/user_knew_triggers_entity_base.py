from src import typing
from python_library.src import sa
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc

from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='user_knew_triggers_entity_base')

class user_knew_triggers_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー知ったきっかけテーブルエンティティの基底クラス
    """
    __abstract__: bool = True

    @saed.declared_attr
    def user_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.BIGINT(unsigned = True), sa.ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @saed.declared_attr
    def knew_trigger_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), sa.ForeignKey('knew_triggers.knew_trigger_id'), nullable = False, server_default = '0', primary_key = True, comment = '知ったきっかけID')
    @saed.declared_attr
    def knew_triggers(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('knew_triggers_entity', back_populates='user_knew_triggers_collection', cascade='merge,save-update', uselist=False)
    @saed.declared_attr
    def users(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('users_entity', back_populates='user_knew_triggers_collection', cascade='merge,save-update', uselist=False)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['user_id', 'knew_trigger_id', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['user_id', 'knew_trigger_id', 'updated_at']
