from src.database import db
from src.model.entity import declared_attr, entity, TINYINT, my_varbinary, BIGINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty

T = TypeVar('T', bound='contact_methods_entity_base')

class contact_methods_entity_base(timestamp_mixin_entity, entity):
    """
    連絡方法マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __CONTACT_METHOD_NAME_LENGTH: int = 32

    def get_contact_method_name_length(cls: Type[T]) -> int:
        return contact_methods_entity_base.__CONTACT_METHOD_NAME_LENGTH

    @declared_attr
    def contact_method_id(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '連絡方法ID')
    @declared_attr
    def contact_method_name(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(contact_methods_entity_base.__CONTACT_METHOD_NAME_LENGTH), nullable = False, server_default = '', comment = '連絡方法名')
    @declared_attr
    def user_contact_methods_collection(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('user_contact_methods_entity', back_populates='contact_methods', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: Type[T]) -> List[str]:
        return ['contact_method_name', 'created_at', 'updated_at']
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['contact_method_name', 'updated_at']
