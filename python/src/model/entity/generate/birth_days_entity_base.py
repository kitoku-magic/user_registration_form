from src.model.entity import declared_attr, entity, SMALLINT, DATE, BIGINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty
from src.model.repository import repository

T = TypeVar('T', bound='birth_days_entity_base')

class birth_days_entity_base(timestamp_mixin_entity, entity):
    """
    誕生日マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True

    @declared_attr
    def birth_day_id(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(SMALLINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '誕生日ID')
    @declared_attr
    def birth_day(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(DATE(), nullable = False, server_default = '0001-01-01', comment = '誕生日')
    @declared_attr
    def users_collection(cls: Type[T]) -> RelationshipProperty:
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='birth_days', cascade='save-update, merge, delete', uselist=True)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['birth_day']
