from src.model import *
from src.model.generate import *

class sexes_base(timestamp_mixin, model):
    __abstract__ = True
    __SEX_NAME_LENGTH = 32

    def get_sex_name_length(cls):
        return sexes_base.__SEX_NAME_LENGTH

    @declared_attr
    def sex_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '性別ID')
    @declared_attr
    def sex_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(sexes_base.__SEX_NAME_LENGTH), nullable = False, server_default = '', comment = '性別名')
    @declared_attr
    def users_collection(cls):
        return model.get_db_instance(model).relationship('users', back_populates='sexes', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        model.__init__(self)
