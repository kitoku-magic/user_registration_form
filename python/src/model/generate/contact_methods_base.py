from src.model import *
from src.model.generate import *

class contact_methods_base(timestamp_mixin, model):
    __abstract__ = True
    contact_method_name_length = 32

    @declared_attr
    def contact_method_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '連絡方法ID')
    @declared_attr
    def contact_method_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(contact_methods_base.contact_method_name_length), nullable = False, server_default = '', comment = '連絡方法名')
    @declared_attr
    def user_contact_methods_collection(cls):
        return model.get_db_instance(model).relationship('user_contact_methods', back_populates='contact_methods', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
