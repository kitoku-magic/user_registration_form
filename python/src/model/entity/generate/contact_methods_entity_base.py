from src import typing
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc
from python_library.src.custom_sqlalchemy.custom_varbinary import custom_varbinary
from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='contact_methods_entity_base')

class contact_methods_entity_base(timestamp_mixin_entity, entity):
    """
    連絡方法マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __CONTACT_METHOD_NAME_LENGTH: int = 32

    def get_contact_method_name_length(cls: typing.Type[T]) -> int:
        return contact_methods_entity_base.__CONTACT_METHOD_NAME_LENGTH

    @saed.declared_attr
    def contact_method_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '連絡方法ID')
    @saed.declared_attr
    def contact_method_name(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(contact_methods_entity_base.__CONTACT_METHOD_NAME_LENGTH), nullable = False, server_default = '', comment = '連絡方法名')
    @saed.declared_attr
    def user_contact_methods_collection(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('user_contact_methods_entity', back_populates='contact_methods', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['contact_method_name', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['contact_method_name', 'updated_at']
