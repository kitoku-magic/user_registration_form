from src.database import db
from src.model.entity import declared_attr, entity, TINYINT, my_varbinary, BIGINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty

T = TypeVar('T', bound='knew_triggers_entity_base')

class knew_triggers_entity_base(timestamp_mixin_entity, entity):
    """
    知ったきっかけマスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __KNEW_TRIGGER_NAME_LENGTH: int = 64

    def get_knew_trigger_name_length(cls: Type[T]) -> int:
        return knew_triggers_entity_base.__KNEW_TRIGGER_NAME_LENGTH

    @declared_attr
    def knew_trigger_id(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '知ったきっかけID')
    @declared_attr
    def knew_trigger_name(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(knew_triggers_entity_base.__KNEW_TRIGGER_NAME_LENGTH), nullable = False, server_default = '', comment = '知ったきっかけ名')
    @declared_attr
    def user_knew_triggers_collection(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('user_knew_triggers_entity', back_populates='knew_triggers', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: Type[T]) -> List[str]:
        return ['knew_trigger_name', 'created_at', 'updated_at']
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['knew_trigger_name', 'updated_at']
