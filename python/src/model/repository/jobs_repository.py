from src.model.repository import *

class jobs_repository(repository):
    def __init__(self, jobs_entity):
        super().__init__(jobs_entity)
