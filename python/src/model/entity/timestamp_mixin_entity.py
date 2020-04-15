from src.database import db
from src.model.entity import *

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
        return db.Column(BIGINT(unsigned = True), nullable = False, server_default = '0', comment = '作成日時のタイムスタンプ')
    @declared_attr
    def updated_at(cls):
        return db.Column(BIGINT(unsigned = True), nullable = False, server_default = '0', comment = '更新日時のタイムスタンプ')
