from src.model import *

class pre_users(pre_users_base):
    def __init__(self):
        super().__init__()
    @validates('mail_address')
    def validate_mail_address(self, key, value):
        # TODO: この辺は、app.configから取りたい
        #print(setting)
        #print(setting.app)
        #print(setting.app.config)
        errors = self.get_validate_errors()
        if value == '':
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスが未入力です'})
        #elif self.mail_address_length < len(value.encode(setting.app.config['PG_CHARACTER_SET'])):
        elif self.mail_address_length < len(value.encode('utf-8')):
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスは入力可能桁数を超えています'})
        elif '@' not in value:
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスの書式が不正です'})
        return value
