from src.model import *
from src.model.generate import *

class jobs_base(timestamp_mixin, model):
    __abstract__ = True
    __JOB_NAME_LENGTH = 32

    def get_job_name_length(cls):
        return jobs_base.__JOB_NAME_LENGTH

    @declared_attr
    def job_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '職業ID')
    @declared_attr
    def job_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(jobs_base.__JOB_NAME_LENGTH), nullable = False, server_default = '', comment = '職業名')
    @declared_attr
    def users_collection(cls):
        return model.get_db_instance(model).relationship('users', back_populates='jobs', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        model.__init__(self)
