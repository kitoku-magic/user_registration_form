from src.model import *
from src.model.generate import *

class user_contact_methods_base(timestamp_mixin, model):
    __abstract__ = True

    @declared_attr
    def user_id(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), model.get_db_instance(model).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def contact_method_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('contact_methods.contact_method_id'), nullable = False, server_default = '0', primary_key = True, comment = '連絡方法ID')
    @declared_attr
    def contact_methods(cls):
        return model.get_db_instance(model).relationship('contact_methods', back_populates='user_contact_methods_collection', uselist=False)
    @declared_attr
    def users(cls):
        return model.get_db_instance(model).relationship('users', back_populates='user_contact_methods_collection', uselist=False)
    def __init__(self):
        model.__init__(self)
