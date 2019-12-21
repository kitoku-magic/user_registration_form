from src.model import *

class contact_methods_base(timestamp_mixin, model):
    __tablename__ = 'contact_methods'
    contact_method_name_length = 32
    contact_method_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '連絡方法ID')
    contact_method_name = model.get_db_instance(model).Column(VARBINARY(contact_method_name_length), nullable = False, server_default = '', comment = '連絡方法名')

    user_contact_methods_collection = model.get_db_instance(model).relationship('user_contact_methods_base', back_populates='contact_methods', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
