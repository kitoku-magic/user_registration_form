from src.model.entity import *
from src.model.entity.generate import *
from src.model.repository import repository

class users_entity_base(timestamp_mixin_entity, entity):
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

    def get_all_properties(self):
        return {
            'user_id' : 0,
            'mail_address' : '',
            'token' : '',
            'registration_status' : 0,
            'last_name' : '',
            'first_name' : '',
            'last_name_hiragana' : '',
            'first_name_hiragana' : '',
            'sex_id' : 0,
            'birth_day_id' : 0,
            'zip_code' : '',
            'prefecture_id' : 0,
            'city_street_address' : '',
            'building_room_address' : '',
            'telephone_number' : '',
            'job_id' : 0,
            'job_other' : '',
            'is_latest_news_hoped' : 0,
            'file_name' : '',
            'file_path' : '',
            'remarks' : '',
            'is_personal_information_provide_agreed' : 0,
            'created_at' : 0,
            'updated_at' : 0,
            'sexes' : [],
            'prefectures' : [],
            'birth_days' : [],
            'jobs' : [],
            'user_contact_methods_collection' : [],
            'user_knew_triggers_collection' : [],
        }

    def get_mail_address_length(cls):
        return users_entity_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls):
        return users_entity_base.__TOKEN_LENGTH
    def get_last_name_length(cls):
        return users_entity_base.__LAST_NAME_LENGTH
    def get_first_name_length(cls):
        return users_entity_base.__FIRST_NAME_LENGTH
    def get_last_name_hiragana_length(cls):
        return users_entity_base.__LAST_NAME_HIRAGANA_LENGTH
    def get_first_name_hiragana_length(cls):
        return users_entity_base.__FIRST_NAME_HIRAGANA_LENGTH
    def get_zip_code_length(cls):
        return users_entity_base.__ZIP_CODE_LENGTH
    def get_city_street_address_length(cls):
        return users_entity_base.__CITY_STREET_ADDRESS_LENGTH
    def get_building_room_address_length(cls):
        return users_entity_base.__BUILDING_ROOM_ADDRESS_LENGTH
    def get_telephone_number_length(cls):
        return users_entity_base.__TELEPHONE_NUMBER_LENGTH
    def get_job_other_length(cls):
        return users_entity_base.__JOB_OTHER_LENGTH
    def get_file_name_length(cls):
        return users_entity_base.__FILE_NAME_LENGTH
    def get_file_path_length(cls):
        return users_entity_base.__FILE_PATH_LENGTH

    @declared_attr
    def user_id(cls):
        return repository.get_db_instance(repository).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')
    @declared_attr
    def registration_status(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '登録状況')
    @declared_attr
    def last_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__LAST_NAME_LENGTH), nullable = False, server_default = '', comment = '苗字')
    @declared_attr
    def first_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__FIRST_NAME_LENGTH), nullable = False, server_default = '', comment = '名前')
    @declared_attr
    def last_name_hiragana(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__LAST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '苗字（ひらがな）')
    @declared_attr
    def first_name_hiragana(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__FIRST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '名前（ひらがな）')
    @declared_attr
    def sex_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('sexes.sex_id'), nullable = False, server_default = '0', comment = '性別ID')
    @declared_attr
    def birth_day_id(cls):
        return repository.get_db_instance(repository).Column(SMALLINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('birth_days.birth_day_id'), nullable = False, server_default = '0', comment = '誕生日ID')
    @declared_attr
    def zip_code(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__ZIP_CODE_LENGTH), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_street_address(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__CITY_STREET_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '市区町村・丁目・番地')
    @declared_attr
    def building_room_address(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__BUILDING_ROOM_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '建物名・室名')
    @declared_attr
    def telephone_number(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__TELEPHONE_NUMBER_LENGTH), nullable = False, server_default = '', comment = '電話番号')
    @declared_attr
    def job_id(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), repository.get_db_instance(repository).ForeignKey('jobs.job_id'), nullable = False, server_default = '0', comment = '職業ID')
    @declared_attr
    def job_other(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__JOB_OTHER_LENGTH), nullable = False, server_default = '', comment = '職業その他')
    @declared_attr
    def is_latest_news_hoped(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '最新情報の希望状況')
    @declared_attr
    def file_name(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__FILE_NAME_LENGTH), nullable = False, server_default = '', comment = 'ファイル名')
    @declared_attr
    def file_path(cls):
        return repository.get_db_instance(repository).Column(VARBINARY(users_entity_base.__FILE_PATH_LENGTH), nullable = False, server_default = '', comment = 'ファイルパス')
    @declared_attr
    def remarks(cls):
        return repository.get_db_instance(repository).Column(BLOB(), nullable = False, comment = '備考')
    @declared_attr
    def is_personal_information_provide_agreed(cls):
        return repository.get_db_instance(repository).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '個人情報提供の同意状況')
    @declared_attr
    def sexes(cls):
        return repository.get_db_instance(repository).relationship('sexes_entity', back_populates='users_collection', uselist=False)
    @declared_attr
    def prefectures(cls):
        return repository.get_db_instance(repository).relationship('prefectures_entity', back_populates='users_collection', uselist=False)
    @declared_attr
    def birth_days(cls):
        return repository.get_db_instance(repository).relationship('birth_days_entity', back_populates='users_collection', uselist=False)
    @declared_attr
    def jobs(cls):
        return repository.get_db_instance(repository).relationship('jobs_entity', back_populates='users_collection', uselist=False)
    @declared_attr
    def user_contact_methods_collection(cls):
        return repository.get_db_instance(repository).relationship('user_contact_methods_entity', back_populates='users', cascade='save-update, merge, delete', uselist=True)
    @declared_attr
    def user_knew_triggers_collection(cls):
        return repository.get_db_instance(repository).relationship('user_knew_triggers_entity', back_populates='users', cascade='save-update, merge, delete', uselist=True)

    def __init__(self):
        timestamp_mixin_entity.__init__(self)