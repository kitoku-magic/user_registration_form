from src.model import *

class user(timestamp_mixin, model):
    mail_address_length = 512
    user_id = model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True)
    mail_address = model.get_db_instance(model).Column(VARBINARY(mail_address_length), nullable = False, server_default = '', unique = True)
    token = model.get_db_instance(model).Column(VARBINARY(128), nullable = False, server_default = '')
    registration_status = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0')
    last_name = model.get_db_instance(model).Column(VARBINARY(32), nullable = False, server_default = '')
    first_name = model.get_db_instance(model).Column(VARBINARY(32), nullable = False, server_default = '')
    last_name_hiragana = model.get_db_instance(model).Column(VARBINARY(64), nullable = False, server_default = '')
    first_name_hiragana = model.get_db_instance(model).Column(VARBINARY(64), nullable = False, server_default = '')
    sex_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0')
    birth_day = model.get_db_instance(model).Column(DATE, nullable = False, server_default = '0001-01-01')
    zip_code = model.get_db_instance(model).Column(VARBINARY(8), nullable = False, server_default = '')
    prefectures_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0')
    city_street_address = model.get_db_instance(model).Column(VARBINARY(256), nullable = False, server_default = '')
    building_room_address = model.get_db_instance(model).Column(VARBINARY(256), nullable = False, server_default = '')
    telephone_number = model.get_db_instance(model).Column(VARBINARY(13), nullable = False, server_default = '')
    job_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0')
    job_other = model.get_db_instance(model).Column(VARBINARY(64), nullable = False, server_default = '')
    is_latest_news_hoped = model.get_db_instance(model).Column(BOOLEAN, nullable = False, server_default = '0')
    file_name = model.get_db_instance(model).Column(VARBINARY(256), nullable = False, server_default = '')
    file_path = model.get_db_instance(model).Column(VARBINARY(512), nullable = False, server_default = '')
    remarks = model.get_db_instance(model).Column(BLOB, nullable = False)
    is_personal_information_provide_agreed = model.get_db_instance(model).Column(BOOLEAN, nullable = False, server_default = '0')
    def __init__(self):
        super().__init__()
        # BLOB型はデフォルト値が設定出来ない為
        self.remarks = bytearray('', 'utf-8')
        self.created_at = 0
        self.updated_at = 0
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
