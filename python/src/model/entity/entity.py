from src.database import db
from src.model.entity import *

class entity(db.Model):
    __abstract__ = True
    def __init__(self):
        self.__validate_errors = {'result': True, 'error': []}
        property_dict = self.get_all_properties()
        for field, value in property_dict.items():
            setattr(self, field, value)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower().replace('_entity', '')
    def get_validate_errors(self):
        return self.__validate_errors
    def set_request_to_entity(self, request_data):
        properties = self.get_all_properties()
        request_data = request_data.to_dict()
        for field, value in properties.items():
            is_exist = False
            for k, v in request_data.items():
                if field == k:
                    is_exist = True
                    if str == type(v) and True == v.isdecimal():
                        v = int(v)
                    setattr(self, field, v)
                    break
            if False == is_exist and value != []:
                setattr(self, field, None)
    def trim_all_data(self):
        properties = self.get_all_properties()
        for field, value in properties.items():
            if str == type(value):
                # 改行コードはtrimしない
                setattr(self, field, util.mb_trim(value, '\u0020\u0009\u0000\u000b\u3000'))
    def get_all_properties(self):
        attributes = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        property_dict = {}
        for attribute in attributes:
            if 'metadata' == attribute[0] or 'query' == attribute[0] or 'query_class' == attribute[0]:
                continue
            if True == attribute[0].startswith('_'):
                continue
            property_dict[attribute[0]] = attribute[1]
        return property_dict
    @validates('mail_address')
    def validate_mail_address(self, key, value):
        # クラスインスタンス生成時の変数初期化の際は、バリデーションしない
        if value is None and getattr(self, key) is None:
            return value
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
