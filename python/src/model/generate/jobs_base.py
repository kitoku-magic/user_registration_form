from src.model import *

class jobs_base(timestamp_mixin, model):
    __tablename__ = 'jobs'
    job_name_length = 32
    job_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '職業ID')
    job_name = model.get_db_instance(model).Column(VARBINARY(job_name_length), nullable = False, server_default = '', comment = '職業名')

    users_collection = model.get_db_instance(model).relationship('users_base', back_populates='jobs', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
