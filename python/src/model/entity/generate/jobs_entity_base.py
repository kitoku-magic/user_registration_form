from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class jobs_entity_base(timestamp_mixin_entity, entity):
    __abstract__ = True
    __JOB_NAME_LENGTH = 32

    def get_job_name_length(cls):
        return jobs_entity_base.__JOB_NAME_LENGTH

    @declared_attr
    def job_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '職業ID')
    @declared_attr
    def job_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(jobs_entity_base.__JOB_NAME_LENGTH), nullable = False, server_default = '', comment = '職業名')
    @declared_attr
    def users_collection(cls):
        return repository.get_db_instance(repository).relationship('users_entity', back_populates='jobs', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)
