from src import typing
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc
from python_library.src.custom_sqlalchemy.custom_varbinary import custom_varbinary
from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='knew_triggers_entity_base')

class knew_triggers_entity_base(timestamp_mixin_entity, entity):
    """
    知ったきっかけマスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __KNEW_TRIGGER_NAME_LENGTH: int = 64

    def get_knew_trigger_name_length(cls: typing.Type[T]) -> int:
        return knew_triggers_entity_base.__KNEW_TRIGGER_NAME_LENGTH

    @saed.declared_attr
    def knew_trigger_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '知ったきっかけID')
    @saed.declared_attr
    def knew_trigger_name(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(knew_triggers_entity_base.__KNEW_TRIGGER_NAME_LENGTH), nullable = False, server_default = '', comment = '知ったきっかけ名')
    @saed.declared_attr
    def user_knew_triggers_collection(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('user_knew_triggers_entity', back_populates='knew_triggers', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['knew_trigger_name', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['knew_trigger_name', 'updated_at']
