from src.model import *

class timestamp_mixin(model):
    __abstract__ = True
    def __init__(self):
        self.created_at = 0
        self.updated_at = 0
    @declared_attr
    def created_at(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, server_default = '0')
    @declared_attr
    def updated_at(cls):
        return  model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, server_default = '0')
