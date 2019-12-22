from src.model import *
from src.model.generate import *

class users_base(timestamp_mixin, model):
    __abstract__ = True
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

    @declared_attr
    def user_id(cls):
        return model.get_db_instance(model).Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.mail_address_length), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.token_length), nullable = False, server_default = '', comment = 'トークン値')
    @declared_attr
    def registration_status(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '登録状況')
    @declared_attr
    def last_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.last_name_length), nullable = False, server_default = '', comment = '苗字')
    @declared_attr
    def first_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.first_name_length), nullable = False, server_default = '', comment = '名前')
    @declared_attr
    def last_name_hiragana(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.last_name_hiragana_length), nullable = False, server_default = '', comment = '苗字（ひらがな）')
    @declared_attr
    def first_name_hiragana(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.first_name_hiragana_length), nullable = False, server_default = '', comment = '名前（ひらがな）')
    @declared_attr
    def sex_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('sexes.sex_id'), nullable = False, server_default = '0', comment = '性別ID')
    @declared_attr
    def birth_day_id(cls):
        return model.get_db_instance(model).Column(SMALLINT(unsigned = True), model.get_db_instance(model).ForeignKey('birth_days.birth_day_id'), nullable = False, server_default = '0', comment = '誕生日ID')
    @declared_attr
    def zip_code(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.zip_code_length), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_street_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.city_street_address_length), nullable = False, server_default = '', comment = '市区町村・丁目・番地')
    @declared_attr
    def building_room_address(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.building_room_address_length), nullable = False, server_default = '', comment = '建物名・室名')
    @declared_attr
    def telephone_number(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.telephone_number_length), nullable = False, server_default = '', comment = '電話番号')
    @declared_attr
    def job_id(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), model.get_db_instance(model).ForeignKey('jobs.job_id'), nullable = False, server_default = '0', comment = '職業ID')
    @declared_attr
    def job_other(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.job_other_length), nullable = False, server_default = '', comment = '職業その他')
    @declared_attr
    def is_latest_news_hoped(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '最新情報の希望状況')
    @declared_attr
    def file_name(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.file_name_length), nullable = False, server_default = '', comment = 'ファイル名')
    @declared_attr
    def file_path(cls):
        return model.get_db_instance(model).Column(VARBINARY(users_base.file_path_length), nullable = False, server_default = '', comment = 'ファイルパス')
    @declared_attr
    def remarks(cls):
        return model.get_db_instance(model).Column(BLOB(), nullable = False, comment = '備考')
    @declared_attr
    def is_personal_information_provide_agreed(cls):
        return model.get_db_instance(model).Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '個人情報提供の同意状況')
    @declared_attr
    def prefectures(cls):
        return model.get_db_instance(model).relationship('prefectures', back_populates='users_collection', uselist=False)
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
    def user_knew_triggers_collection(cls):
        return model.get_db_instance(model).relationship('user_knew_triggers', back_populates='users', cascade='save-update, merge, delete', uselist=True)
    @declared_attr
    def user_contact_methods_collection(cls):
        return model.get_db_instance(model).relationship('user_contact_methods', back_populates='users', cascade='save-update, merge, delete', uselist=True)
    def __init__(self):
        model.__init__(self)
