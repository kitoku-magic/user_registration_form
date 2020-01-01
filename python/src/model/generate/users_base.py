from src.model import *
from src.model.generate import *

class users_base(timestamp_mixin, model):
    __abstract__ = True
    __MAIL_ADDRESS_LENGTH = 512
    __TOKEN_LENGTH = 128
    __LAST_NAME_LENGTH = 32
    __FIRST_NAME_LENGTH = 32
    __LAST_NAME_HIRAGANA_LENGTH = 64
    __FIRST_NAME_HIRAGANA_LENGTH = 64
    __ZIP_CODE_LENGTH = 8
    __CITY_STREET_ADDRESS_LENGTH = 256
    __BUILDING_ROOM_ADDRESS_LENGTH = 128
    __TELEPHONE_NUMBER_LENGTH = 13
    __JOB_OTHER_LENGTH = 64
    __FILE_NAME_LENGTH = 256
    __FILE_PATH_LENGTH = 512

    def get_mail_address_length(cls):
        return users_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls):
        return users_base.__TOKEN_LENGTH
    def get_last_name_length(cls):
        return users_base.__LAST_NAME_LENGTH
    def get_first_name_length(cls):
        return users_base.__FIRST_NAME_LENGTH
    def get_last_name_hiragana_length(cls):
        return users_base.__LAST_NAME_HIRAGANA_LENGTH
    def get_first_name_hiragana_length(cls):
        return users_base.__FIRST_NAME_HIRAGANA_LENGTH
    def get_zip_code_length(cls):
        return users_base.__ZIP_CODE_LENGTH
    def get_city_street_address_length(cls):
        return users_base.__CITY_STREET_ADDRESS_LENGTH
    def get_building_room_address_length(cls):
        return users_base.__BUILDING_ROOM_ADDRESS_LENGTH
    def get_telephone_number_length(cls):
        return users_base.__TELEPHONE_NUMBER_LENGTH
    def get_job_other_length(cls):
        return users_base.__JOB_OTHER_LENGTH
    def get_file_name_length(cls):
        return users_base.__FILE_NAME_LENGTH
    def get_file_path_length(cls):
        return users_base.__FILE_PATH_LENGTH

    @declared_attr
    def user_id(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')
    @declared_attr
    def registration_status(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '登録状況')
    @declared_attr
    def last_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__LAST_NAME_LENGTH), nullable = False, server_default = '', comment = '苗字')
    @declared_attr
    def first_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__FIRST_NAME_LENGTH), nullable = False, server_default = '', comment = '名前')
    @declared_attr
    def last_name_hiragana(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__LAST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '苗字（ひらがな）')
    @declared_attr
    def first_name_hiragana(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__FIRST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '名前（ひらがな）')
    @declared_attr
    def sex_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('sexes.sex_id'), nullable = False, server_default = '0', comment = '性別ID')
    @declared_attr
    def birth_day_id(cls):
        return model.get_db_instance(model).Column(SMALLINT(unsigned = True), model.get_db_instance(model).ForeignKey('birth_days.birth_day_id'), nullable = False, server_default = '0', comment = '誕生日ID')
    @declared_attr
    def zip_code(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__ZIP_CODE_LENGTH), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_street_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__CITY_STREET_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '市区町村・丁目・番地')
    @declared_attr
    def building_room_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__BUILDING_ROOM_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '建物名・室名')
    @declared_attr
    def telephone_number(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__TELEPHONE_NUMBER_LENGTH), nullable = False, server_default = '', comment = '電話番号')
    @declared_attr
    def job_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('jobs.job_id'), nullable = False, server_default = '0', comment = '職業ID')
    @declared_attr
    def job_other(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__JOB_OTHER_LENGTH), nullable = False, server_default = '', comment = '職業その他')
    @declared_attr
    def is_latest_news_hoped(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '最新情報の希望状況')
    @declared_attr
    def file_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__FILE_NAME_LENGTH), nullable = False, server_default = '', comment = 'ファイル名')
    @declared_attr
    def file_path(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.__FILE_PATH_LENGTH), nullable = False, server_default = '', comment = 'ファイルパス')
    @declared_attr
    def remarks(cls):
        return model.get_db_instance(model).Column(BLOB(), nullable = False, comment = '備考')
    @declared_attr
    def is_personal_information_provide_agreed(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '個人情報提供の同意状況')
    @declared_attr
    def birth_days(cls):
        return model.get_db_instance(model).relationship('birth_days', back_populates='users_collection', uselist=False)
    @declared_attr
    def jobs(cls):
        return model.get_db_instance(model).relationship('jobs', back_populates='users_collection', uselist=False)
    @declared_attr
    def sexes(cls):
        return model.get_db_instance(model).relationship('sexes', back_populates='users_collection', uselist=False)
    @declared_attr
    def prefectures(cls):
        return model.get_db_instance(model).relationship('prefectures', back_populates='users_collection', uselist=False)
    @declared_attr
    def user_knew_triggers_collection(cls):
        return model.get_db_instance(model).relationship('user_knew_triggers', back_populates='users', cascade='save-update, merge, delete', uselist=True)
    @declared_attr
    def user_contact_methods_collection(cls):
        return model.get_db_instance(model).relationship('user_contact_methods', back_populates='users', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        model.__init__(self)
