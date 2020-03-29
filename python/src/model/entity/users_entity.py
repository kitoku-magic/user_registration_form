from src.model.entity import *
from src.model.entity.generate import *

class users_entity(users_entity_base):
    def __init__(self):
        super().__init__()
        self.birth_year = ''
        self.birth_month = ''
        self.birth_day = ''
        # BLOB型はデフォルト値が設定出来ない為
        self.remarks = ''
        self.clicked_button = None
        self.zip_code_error = None
    def set_validation_setting(self):
        validation_settings = [
            {
                'name': 'mail_address',
                'show_name': 'メールアドレス',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_mail_address_length()},
                    'mail_format': {},
                    'mail_domain': {},
                },
            },
            {
                'name': 'last_name',
                'show_name': '氏名（姓）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_last_name_length()},
                    'japanese': {},
                },
            },
            {
                'name': 'first_name',
                'show_name': '氏名（名）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_first_name_length()},
                    'japanese': {},
                },
            },
            {
                'name': 'last_name_hiragana',
                'show_name': '氏名（ひらがな）（姓）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_last_name_hiragana_length()},
                    'hiragana': {},
                },
            },
            {
                'name': 'first_name_hiragana',
                'show_name': '氏名（ひらがな）（名）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_first_name_hiragana_length()},
                    'hiragana': {},
                },
            },
            {
                'name': 'sex_id',
                'show_name': '性別',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1, 'max': 3},
                },
            },
            {
                'name': 'birth_year',
                'show_name': '誕生日（年）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1900, 'max': 2019},
                },
            },
            {
                'name': 'birth_month',
                'show_name': '誕生日（月）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1, 'max': 12},
                },
            },
            {
                'name': 'birth_day',
                'show_name': '誕生日（日）',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1, 'max': 31},
                },
            },
            {
                'name': 'birth_day_full',
                'show_name': '誕生日',
                'rules': {
                    'allow_empty': {},
                    'date': {'format': '%Y-%m-%d'},
                },
            },
            {
                'name': 'zip_code',
                'show_name': '郵便番号',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_zip_code_length() + 1},
                    'zip_code_format': {'is_include_hyphen': True},
                },
            },
            {
                'name': 'prefecture_id',
                'show_name': '都道府県',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1, 'max': 47},
                },
            },
            {
                'name': 'city_street_address',
                'show_name': '市区町村・丁目・番地',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_city_street_address_length()},
                    'japanese_extend': {},
                },
            },
            {
                'name': 'building_room_address',
                'show_name': '建物名・室名',
                'rules': {
                    'allow_empty': {},
                    'max_length': {'value': self.get_building_room_address_length()},
                    'japanese_extend': {},
                },
            },
            {
                'name': 'telephone_number',
                'show_name': '電話番号',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'max_length': {'value': self.get_telephone_number_length()},
                    'telephone_format': {'is_include_hyphen': True},
                },
            },
            {
                'name': 'job_id',
                'show_name': '職業',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1, 'max': 6},
                },
            },
        ]

        job_other_setting = {
            'name': 'job_other',
            'show_name': '職業その他',
        }

        rules = {}
        # 職業でその他を選択時のみ必須
        if setting.app.config['JOB_ID_OTHER'] == self.job_id:
            rules['required'] = {}
            rules['not_empty'] = {}
        else:
            rules['allow_empty'] = {}

        rules['max_length'] = {'value': self.get_job_other_length()}
        rules['japanese_extend'] = {}

        job_other_setting['rules'] = rules

        validation_settings.append(job_other_setting)

        add_validation_settings = [
            {
                'name': 'user_contact_methods_collection',
                'show_name': '連絡方法',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {'field': 'contact_method_id'},
                    'range': {'min': 1, 'max': 4, 'field': 'contact_method_id'},
                },
            },
            {
                'name': 'user_knew_triggers_collection',
                'show_name': '知ったきっかけ',
                'rules': {
                    'allow_empty': {},
                    'integer': {'field': 'knew_trigger_id'},
                    'range': {'min': 1, 'max': 6, 'field': 'knew_trigger_id'},
                },
            },
            {
                'name': 'is_latest_news_hoped',
                'show_name': '最新情報の希望状況',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 0, 'max': 1},
                },
            },
            {
                'name': 'file_name',
                'show_name': '添付ファイル',
                'rules': {
                    'file_upload': {
                        'required': False,
                        'allow_mime_types': {
                            'image/gif': True,
                            'image/png': True,
                            'image/jpeg': True,
                            'application/pdf': True,
                            'application/vnd.ms-excel': True,
                            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': True,
                            'application/msword': True,
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': True,
                        },
                        'allow_extensions': {
                            'image/gif': {'gif': True},
                            'image/png': {'png': True},
                            'image/jpeg': {'jpg': True, 'jpeg': True},
                            'application/pdf': {'pdf': True},
                            'application/vnd.ms-excel': {'xls': True},
                            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': {'xlsx': True},
                            'application/msword': {'doc': True},
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': {'docx': True},
                        },
                        'is_file_name_check': True,
                        'max_length': self.get_file_name_length(),
                        'save_path_identifier': setting.app.config['FILE_UPLOAD_IDENTIFIER_USER_REGISTRATION'],
                        'is_secret': True,
                        'path': 'file_path',
                    },
                },
            },
            {
                'name': 'remarks',
                'show_name': '備考',
                'rules': {
                    'allow_empty': {},
                    'max_length': {'value': 1000},
                },
            },
            {
                'name': 'is_personal_information_provide_agreed',
                'show_name': '個人情報提供の同意状況',
                'rules': {
                    'required': {},
                    'not_empty': {},
                    'integer': {},
                    'range': {'min': 1, 'max': 1},
                },
            },
        ]

        validation_settings = validation_settings + add_validation_settings

        for validation_setting in validation_settings:
            self.add_validation_settings(
                validation_setting['name'],
                validation_setting['show_name'],
                validation_setting['rules']
            )
