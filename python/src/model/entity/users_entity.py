from src.model.entity import *
from src.model.entity.generate import *

class users_entity(users_entity_base):
    def __init__(self):
        super().__init__()
        # BLOB型はデフォルト値が設定出来ない為
        self.remarks = ''
        self.clicked_button = None
