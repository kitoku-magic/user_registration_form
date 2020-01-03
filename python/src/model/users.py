from src.model import *
from src.model.generate import *

class users(users_base):
    def __init__(self):
        super().__init__()
        # BLOB型はデフォルト値が設定出来ない為
        self.remarks = ''
