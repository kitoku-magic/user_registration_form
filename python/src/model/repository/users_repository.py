from src.model.repository import *

class users_repository(repository):
    def __init__(self, users_entity):
        super().__init__(users_entity)
