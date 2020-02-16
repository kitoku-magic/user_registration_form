from src.database import db
from src.model.entity import *

class entity(db.Model):
    __abstract__ = True
    def __init__(self):
        self.__validate_errors = {'result': True, 'error': []}

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower().replace('_entity', '')
    def get_validate_errors(self):
        return self.__validate_errors
    def set_request_to_model(self, require_params, request_data):
        for k, v in require_params.items():
            value = request_data.get(k)
            if value is None:
                setattr(self, k, v)
            else:
                setattr(self, k, value)

    @validates('mail_address')
    def validate_mail_address(self, key, value):
        errors = self.get_validate_errors()
        ret = util.check_mail_address(value, self.get_mail_address_length())
        if 1 == ret:
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスが未入力です'})
        elif 2 == ret:
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスは入力可能桁数を超えています'})
        elif 3 == ret:
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスの書式が不正です'})
        elif 4 == ret:
            errors['result'] = False
            errors['error'].append({'name': key, 'message': 'メールアドレスのドメインが存在しません'})
        return value
