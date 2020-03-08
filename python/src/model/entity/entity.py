from src.database import db
from src.model.entity import *

class entity(db.Model):
    __abstract__ = True
    def __init__(self):
        self.__validation_settings = {}
        self.__is_any_item = False
        self.__validate_errors = {'result': True, 'error': []}
        property_dict = self.get_all_properties()
        for field, value in property_dict.items():
            setattr(self, field, value)
#    # 全部完成したらコメントアウトを外す
#    @abstractmethod
#    def set_validation_setting(self):
#        pass
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower().replace('_entity', '')
    def validate(self):
        """
        バリデーションを行う
        """
        result = True
        for name, validation_setting in self.__validation_settings.items():
            # 項目毎に初期化して、前回の状態を引き継がないようにする
            __is_any_item = False
            for rule_name, options in validation_setting['rules'].items():
                method_name = 'is_' + rule_name
                ret = getattr(self, method_name)(getattr(self, name), options)
                if False == ret:
                    result = False
                    if 'message' in options:
                        message = options['message']
                    else:
                        message_format = setting.app.config[rule_name.upper() + '_MESSAGE']
                        message = message_format.replace('{show_name}', validation_setting['show_name']);
                    # エラーメッセージを設定
                    setattr(self, name + '_error', message)
                    # チェックを継続する設定になっていなければ、次の項目へ
                    if 'is_next' not in options or True != options['is_next']:
                        break
        return result
    def is_required(value, options):
        """
        必須項目チェック
        """
        return value is not None
    def is_not_empty(value, options):
        """
        未入力チェック
        """
        return '' != value
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
    def add_validation_settings(self, name, show_name, validation_rules):
        self.__validation_settings[name] = {'show_name': show_name, 'rules': validation_rules}
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
