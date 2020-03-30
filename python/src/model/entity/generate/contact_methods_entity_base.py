from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class contact_methods_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __CONTACT_METHOD_NAME_LENGTH = 32

    def get_contact_method_name_length(cls):
        return contact_methods_entity_base.__CONTACT_METHOD_NAME_LENGTH

    @declared_attr
    def contact_method_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '連絡方法ID')
    @declared_attr
    def contact_method_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(contact_methods_entity_base.__CONTACT_METHOD_NAME_LENGTH), nullable = False, server_default = '', comment = '連絡方法名')
    @declared_attr
    def user_contact_methods_collection(cls):
        return repository.get_db_instance(repository).relationship('user_contact_methods_entity', back_populates='contact_methods', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self):
        pass
    def get_update_column_name_list(self):
        return ['contact_method_name']
