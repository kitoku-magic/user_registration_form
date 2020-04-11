from src.model.entity import declared_attr, entity, TINYINT, VARBINARY, BIGINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty
from src.model.repository import repository

T = TypeVar('T', bound='prefectures_entity_base')

class prefectures_entity_base(timestamp_mixin_entity, entity):
    """
    都道府県マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __PREFECTURE_NAME_LENGTH: int = 12

    def get_prefecture_name_length(cls: Type[T]) -> int:
        return prefectures_entity_base.__PREFECTURE_NAME_LENGTH

    @declared_attr
    def prefecture_id(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '都道府県ID')
    @declared_attr
    def prefecture_name(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(VARBINARY(prefectures_entity_base.__PREFECTURE_NAME_LENGTH), nullable = False, server_default = '', comment = '都道府県名')
    @declared_attr
    def zip_addresses_collection(cls: Type[T]) -> RelationshipProperty:
        return repository.get_db_instance(repository).relationship('zip_addresses_entity', back_populates='prefectures', cascade='save-update, merge, delete', uselist=True)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['prefecture_name']
