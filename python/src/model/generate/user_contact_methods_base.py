from src.model import *

class user_contact_methods_base(timestamp_mixin, model):
    __tablename__ = 'user_contact_methods'
    user_id = model.get_db_instance(model).Column(BIGINT(unsigned = True), model.get_db_instance(model).ForeignKey('users.user_id'), nullable = False, server_default = '0', primary_key = True, comment = 'ユーザーID')
    contact_method_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('contact_methods.contact_method_id'), nullable = False, server_default = '0', primary_key = True, comment = '連絡方法ID')

    users = model.get_db_instance(model).relationship('users_base', back_populates='user_contact_methods_collection', uselist=False)
    contact_methods = model.get_db_instance(model).relationship('contact_methods_base', back_populates='user_contact_methods_collection', uselist=False)
    def __init__(self):
        model.__init__(self)
