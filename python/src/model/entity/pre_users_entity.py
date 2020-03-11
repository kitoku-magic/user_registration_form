from src.model.entity import *
from src.model.entity.generate import *

class pre_users_entity(pre_users_entity_base):
    def __init__(self):
        super().__init__()
    def set_validation_setting(self):
        validation_settings = [
            {
                'name': 'mail_address',
                'show_name': 'メールアドレス',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': 128},
                    'mail_format': {},
                    'mail_domain': {},
                },
            },
        ]

        for validation_setting in validation_settings:
            self.add_validation_settings(
                validation_setting['name'],
                validation_setting['show_name'],
                validation_setting['rules']
            )
