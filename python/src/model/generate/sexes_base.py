from src.model import *

class sexes_base(timestamp_mixin, model):
    __tablename__ = 'sexes'
    sex_name_length = 32
    sex_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '性別ID')
    sex_name = model.get_db_instance(model).Column(VARBINARY(sex_name_length), nullable = False, server_default = '', comment = '性別名')

    users_collection = model.get_db_instance(model).relationship('users_base', back_populates='sexes', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
