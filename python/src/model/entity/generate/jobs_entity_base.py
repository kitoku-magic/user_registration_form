from src.model.entity import declared_attr, entity, TINYINT, VARBINARY, BIGINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty
from src.model.repository import repository

T = TypeVar('T', bound='jobs_entity_base')

class jobs_entity_base(timestamp_mixin_entity, entity):
    """
    職業マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __JOB_NAME_LENGTH: int = 32

    def get_job_name_length(cls: Type[T]) -> int:
        return jobs_entity_base.__JOB_NAME_LENGTH

    @declared_attr
    def job_id(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '職業ID')
    @declared_attr
    def job_name(cls: Type[T]) -> Column:
        return repository.get_db_instance(repository).Column(VARBINARY(jobs_entity_base.__JOB_NAME_LENGTH), nullable = False, server_default = '', comment = '職業名')
    @declared_attr
    def users_collection(cls: Type[T]) -> RelationshipProperty:
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='jobs', cascade='save-update, merge, delete', uselist=True)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['job_name']
