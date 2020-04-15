from src.database import db
from src.model.entity import declared_attr, entity, BIGINT, TINYINT, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty

T = TypeVar('T', bound='user_knew_triggers_entity_base')

class user_knew_triggers_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザー知ったきっかけテーブルエンティティの基底クラス
    """
    __abstract__: bool = True

    @declared_attr
    def user_id(cls: Type[T]) -> Column:
        return db.Column(BIGINT(unsigned = True), db.ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def knew_trigger_id(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), db.ForeignKey('knew_triggers.knew_trigger_id'), nullable = False, server_default = '0', primary_key = True, comment = '知ったきっかけID')
    @declared_attr
    def knew_triggers(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('knew_triggers_entity', back_populates='user_knew_triggers_collection', uselist=False)
    @declared_attr
    def users(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('users_entity', back_populates='user_knew_triggers_collection', uselist=False)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['user_id', 'knew_trigger_id']
