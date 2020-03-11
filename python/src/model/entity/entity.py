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
            self.__is_any_item = False
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
    def is_required(self, value, options):
        """
        必須項目チェック
        """
        return value is not None
    def is_not_empty(self, value, options):
        """
        未入力チェック
        """
        return '' != value and [] != value
    def is_allow_empty(self, value, options):
        """
        未入力を許可する
        """
        self.__is_any_item = True
    def is_min_length(self, value, options):
        """
        最小桁数チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return util.check_min_length(value, options['value'])
        else:
            return True
    def is_max_length(self, value, options):
        """
        最大桁数チェック
        """
        return util.check_max_length(value, options['value'])
    def is_mail_format(self, value, options):
        """
        メール書式チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            r = util.check_mail_format(value)
            return r
        else:
            return True
    def is_mail_domain(self, value, options):
        """
        メールドメインチェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            r = util.check_mail_domain(value)
            return r
        else:
            return True
    def is_alpha_num(self, value, options):
        """
        半角英数字チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return re.match('\A[a-zA-Z0-9]+\Z', value) is not None
        else:
            return True
    def is_japanese(self, value, options):
        """
        日本語（ひらがな、カタカナ、漢字）チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return re.match('\A(?:[' + setting.app.config['PATTERN_HIRAGANA'] + setting.app.config['PATTERN_KATAKANA'] + '][' + setting.app.config['PATTERN_DAKUTEN'] + ']?|' + setting.app.config['PATTERN_CHOON'] + '|' + setting.app.config['PATTERN_KANJI'] + '?)+\Z', value) is not None
        else:
            return True
    def is_japanese_extend(self, value, options):
        """
        日本語（ひらがな、カタカナ、漢字、全角数字、全角スペース）チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return re.match('\A(?:[' + setting.app.config['PATTERN_HIRAGANA'] + setting.app.config['PATTERN_KATAKANA'] + '][' + setting.app.config['PATTERN_DAKUTEN'] + ']?|' + setting.app.config['PATTERN_CHOON'] + '|' + setting.app.config['PATTERN_KANJI'] + '?|[' + setting.app.config['PATTERN_FULL_WIDTH_NUMBER'] + ']|' + setting.app.config['PATTERN_FULL_WIDTH_SPACE'] + ')+\Z', value) is not None
        else:
            return True
    def is_hiragana(self, value, options):
        """
        ひらがなチェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return re.match('\A(?:[' + setting.app.config['PATTERN_HIRAGANA'] + '][' + setting.app.config['PATTERN_DAKUTEN'] + ']?)+\Z', value) is not None
        else:
            return True
    def is_number(self, value, options):
        """
        半角数字チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            if True == isinstance(value, list):
                result = True
                for val in value:
                    result = self.is_number(val, options)
                    if False == result:
                        break
                return result
            else:
                return re.match('\A[0-9]+\Z', value) is not None
        else:
            return True
    def is_integer(self, value, options):
        """
        整数チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            if True == isinstance(value, list):
                result = True
                for val in value:
                    result = self.is_number(val, options)
                    if False == result:
                        break
                return result
            else:
                r = None
                try:
                    r = float(value)
                except ValueError:
                    return False
                else:
                    return r.is_integer()
        else:
            return True
    def is_range(self, value, options):
        """
        数値の範囲チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            if True == isinstance(value, list):
                result = True
                for val in value:
                    result = self.is_range(val, options)
                    if False == result:
                        break
                return result
            else:
                r = None
                try:
                    r = float(value)
                except ValueError:
                    return False
                else:
                    return options['min'] <= r and r <= options['max']
        else:
            return True
    def is_date(self, value, options):
        """
        日付チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return util.check_date(value, options['format'])
        else:
            return True
    def is_zip_code_format(self, value, options):
        """
        郵便番号書式チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return util.check_zip_code(value, options['is_include_hyphen'])
        else:
            return True
    def is_telephone_format(self, value, options):
        """
        電話番号書式チェック
        """
        is_check = self.is_check(value)
        if True == is_check:
            return util.check_telephone(value, options['is_include_hyphen'])
        else:
            return True
    def is_check(self, value):
        """
        チェックをするかどうかを調べる
        """
        result = True
        # 任意項目で且つ、値が空の時はチェックしない
        if True == self.__is_any_item and True == util.is_empty(value):
            result = False
        return result
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
                    if True == isinstance(v, str) and True == v.isdecimal():
                        v = int(v)
                    setattr(self, field, v)
                    break
            if False == is_exist and value != []:
                setattr(self, field, None)
    def trim_all_data(self):
        properties = self.get_all_properties()
        for field, value in properties.items():
            if True == isinstance(value, str):
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
