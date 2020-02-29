from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class user_contact_methods_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True

    def get_all_properties(self):
        return {
            'user_id' : 0,
            'contact_method_id' : 0,
            'created_at' : 0,
            'updated_at' : 0,
            'contact_methods' : [],
            'users' : [],
        }

    @declared_attr
    def user_id(cls):
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def contact_method_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('contact_methods.contact_method_id'), nullable = False, server_default = '0', primary_key = True, comment = '連絡方法ID')
    @declared_attr
    def contact_methods(cls):
        return repository.get_db_instance(repository).relationship('contact_methods_entity', back_populates='user_contact_methods_collection', uselist=False)
    @declared_attr
    def users(cls):
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='user_contact_methods_collection', uselist=False)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)