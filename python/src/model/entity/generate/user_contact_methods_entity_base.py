from src import typing
from python_library.src import sa
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc

from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='user_contact_methods_entity_base')

class user_contact_methods_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー連絡方法テーブルエンティティの基底クラス
    """
    __abstract__: bool = True

    @saed.declared_attr
    def user_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.BIGINT(unsigned = True), sa.ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @saed.declared_attr
    def contact_method_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), sa.ForeignKey('contact_methods.contact_method_id'), nullable = False, server_default = '0', primary_key = True, comment = '連絡方法ID')
    @saed.declared_attr
    def contact_methods(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('contact_methods_entity', back_populates='user_contact_methods_collection', cascade='merge,save-update', uselist=False)
    @saed.declared_attr
    def users(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('users_entity', back_populates='user_contact_methods_collection', cascade='merge,save-update', uselist=False)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['user_id', 'contact_method_id', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['user_id', 'contact_method_id', 'updated_at']
