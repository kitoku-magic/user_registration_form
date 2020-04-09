from src.model.entity import *
from src.model.repository import repository

class timestamp_mixin_entity(entity):
    """
    タイムスタンプを設定するエンティティのミックスイン
    """
    __abstract__ = True
    def __init__(self):
        super().__init__()
        self.created_at = 0
        self.updated_at = 0

    @declared_attr
    def created_at(cls):
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), nullable = False, server_default = '0', comment = '作成日時のタイムスタンプ')
    @declared_attr
    def updated_at(cls):
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), nullable = False, server_default = '0', comment = '更新日時のタイムスタンプ')
