from src.model import *

class users_base(timestamp_mixin, model):
    __tablename__ = 'users'
    mail_address_length = 512
    token_length = 128
    last_name_length = 32
    first_name_length = 32
    last_name_hiragana_length = 64
    first_name_hiragana_length = 64
    zip_code_length = 8
    city_street_address_length = 256
    building_room_address_length = 128
    telephone_number_length = 13
    job_other_length = 64
    file_name_length = 256
    file_path_length = 512
    user_id = model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    mail_address = model.get_db_instance(model).Column(VARBINARY(mail_address_length), nullable = False, server_default = '', comment = 'メールアドレス')
    token = model.get_db_instance(model).Column(VARBINARY(token_length), nullable = False, server_default = '', comment = 'トークン値')
    registration_status = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '登録状況')
    last_name = model.get_db_instance(model).Column(VARBINARY(last_name_length), nullable = False, server_default = '', comment = '苗字')
    first_name = model.get_db_instance(model).Column(VARBINARY(first_name_length), nullable = False, server_default = '', comment = '名前')
    last_name_hiragana = model.get_db_instance(model).Column(VARBINARY(last_name_hiragana_length), nullable = False, server_default = '', comment = '苗字（ひらがな）')
    first_name_hiragana = model.get_db_instance(model).Column(VARBINARY(first_name_hiragana_length), nullable = False, server_default = '', comment = '名前（ひらがな）')
    sex_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('sexes.sex_id'), nullable = False, server_default = '0', comment = '性別ID')
    birth_day_id = model.get_db_instance(model).Column(SMALLINT(unsigned = True), model.get_db_instance(model).ForeignKey('birth_days.birth_day_id'), nullable = False, server_default = '0', comment = '誕生日ID')
    zip_code = model.get_db_instance(model).Column(VARBINARY(zip_code_length), nullable = False, server_default = '', comment = '郵便番号')
    prefecture_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    city_street_address = model.get_db_instance(model).Column(VARBINARY(city_street_address_length), nullable = False, server_default = '', comment = '市区町村・丁目・番地')
    building_room_address = model.get_db_instance(model).Column(VARBINARY(building_room_address_length), nullable = False, server_default = '', comment = '建物名・室名')
    telephone_number = model.get_db_instance(model).Column(VARBINARY(telephone_number_length), nullable = False, server_default = '', comment = '電話番号')
    job_id = model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('jobs.job_id'), nullable = False, server_default = '0', comment = '職業ID')
    job_other = model.get_db_instance(model).Column(VARBINARY(job_other_length), nullable = False, server_default = '', comment = '職業その他')
    is_latest_news_hoped = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '最新情報の希望状況')
    file_name = model.get_db_instance(model).Column(VARBINARY(file_name_length), nullable = False, server_default = '', comment = 'ファイル名')
    file_path = model.get_db_instance(model).Column(VARBINARY(file_path_length), nullable = False, server_default = '', comment = 'ファイルパス')
    remarks = model.get_db_instance(model).Column(BLOB(), nullable = False, comment = '備考')
    is_personal_information_provide_agreed = model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '個人情報提供の同意状況')

    prefectures = model.get_db_instance(model).relationship('prefectures_base', back_populates='users_collection', uselist=False)
    birth_days = model.get_db_instance(model).relationship('birth_days_base', back_populates='users_collection', uselist=False)
    jobs = model.get_db_instance(model).relationship('jobs_base', back_populates='users_collection', uselist=False)
    sexes = model.get_db_instance(model).relationship('sexes_base', back_populates='users_collection', uselist=False)
    user_contact_methods_collection = model.get_db_instance(model).relationship('user_contact_methods_base', back_populates='users', cascade='save-update, merge, delete', uselist=True)
    user_knew_triggers_collection = model.get_db_instance(model).relationship('user_knew_triggers_base', back_populates='users', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
