from src.model import *

class birth_days_base(timestamp_mixin, model):
    __tablename__ = 'birth_days'
    birth_day_id = model.get_db_instance(model).Column(SMALLINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '誕生日ID')
    birth_day = model.get_db_instance(model).Column(DATE(), nullable = False, server_default = '0001-01-01', comment = '誕生日')

    users_collection = model.get_db_instance(model).relationship('users_base', back_populates='birth_days', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
