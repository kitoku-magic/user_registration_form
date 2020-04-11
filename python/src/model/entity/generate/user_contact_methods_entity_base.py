from src.model.entity import declared_attr, entity, BIGINT, TINYINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty
from src.model.repository import repository

T = TypeVar('T', bound='user_contact_methods_entity_base')

class user_contact_methods_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー連絡方法テーブルエンティティの基底クラス
    """
    __abstract__: bool = True

    @declared_attr
    def user_id(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def contact_method_id(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('contact_methods.contact_method_id'), nullable = False, server_default = '0', primary_key = True, comment = '連絡方法ID')
    @declared_attr
    def contact_methods(cls: Type[T]) -> RelationshipProperty:
        return repository.get_db_instance(repository).relationship('contact_methods_entity', back_populates='user_contact_methods_collection', uselist=False)
    @declared_attr
    def users(cls: Type[T]) -> RelationshipProperty:
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='user_contact_methods_collection', uselist=False)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['user_id', 'contact_method_id']
