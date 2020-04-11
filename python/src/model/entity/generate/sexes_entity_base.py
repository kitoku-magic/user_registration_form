from src.model.entity import declared_attr, entity, TINYINT, VARBINARY, BIGINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty
from src.model.repository import repository

T = TypeVar('T', bound='sexes_entity_base')

class sexes_entity_base(timestamp_mixin_entity, entity):
    """
    性別マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __SEX_NAME_LENGTH: int = 32

    def get_sex_name_length(cls: Type[T]) -> int:
        return sexes_entity_base.__SEX_NAME_LENGTH

    @declared_attr
    def sex_id(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '性別ID')
    @declared_attr
    def sex_name(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(VARBINARY(sexes_entity_base.__SEX_NAME_LENGTH), nullable = False, server_default = '', comment = '性別名')
    @declared_attr
    def users_collection(cls: Type[T]) -> RelationshipProperty:
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='sexes', cascade='save-update, merge, delete', uselist=True)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['sex_name']
