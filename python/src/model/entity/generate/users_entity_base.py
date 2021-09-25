from src import typing
from python_library.src import sa
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc
from python_library.src.custom_sqlalchemy.custom_blob import custom_blob
from python_library.src.custom_sqlalchemy.custom_varbinary import custom_varbinary
from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='users_entity_base')

class users_entity_base(timestamp_mixin_entity, entity):
    """
    ユーザーテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __MAIL_ADDRESS_LENGTH: int = 512
    __TOKEN_LENGTH: int = 128
    __LAST_NAME_LENGTH: int = 32
    __FIRST_NAME_LENGTH: int = 32
    __LAST_NAME_HIRAGANA_LENGTH: int = 64
    __FIRST_NAME_HIRAGANA_LENGTH: int = 64
    __ZIP_CODE_LENGTH: int = 7
    __CITY_STREET_ADDRESS_LENGTH: int = 256
    __BUILDING_ROOM_ADDRESS_LENGTH: int = 128
    __TELEPHONE_NUMBER_LENGTH: int = 13
    __JOB_OTHER_LENGTH: int = 64
    __FILE_NAME_LENGTH: int = 256
    __FILE_PATH_LENGTH: int = 512

    def get_mail_address_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__TOKEN_LENGTH
    def get_last_name_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__LAST_NAME_LENGTH
    def get_first_name_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__FIRST_NAME_LENGTH
    def get_last_name_hiragana_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__LAST_NAME_HIRAGANA_LENGTH
    def get_first_name_hiragana_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__FIRST_NAME_HIRAGANA_LENGTH
    def get_zip_code_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__ZIP_CODE_LENGTH
    def get_city_street_address_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__CITY_STREET_ADDRESS_LENGTH
    def get_building_room_address_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__BUILDING_ROOM_ADDRESS_LENGTH
    def get_telephone_number_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__TELEPHONE_NUMBER_LENGTH
    def get_job_other_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__JOB_OTHER_LENGTH
    def get_file_name_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__FILE_NAME_LENGTH
    def get_file_path_length(cls: typing.Type[T]) -> int:
        return users_entity_base.__FILE_PATH_LENGTH

    @saed.declared_attr
    def user_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @saed.declared_attr
    def mail_address(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @saed.declared_attr
    def token(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')
    @saed.declared_attr
    def registration_status(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '登録状況')
    @saed.declared_attr
    def last_name(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__LAST_NAME_LENGTH), nullable = False, server_default = '', comment = '苗字')
    @saed.declared_attr
    def first_name(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__FIRST_NAME_LENGTH), nullable = False, server_default = '', comment = '名前')
    @saed.declared_attr
    def last_name_hiragana(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__LAST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '苗字（ひらがな）')
    @saed.declared_attr
    def first_name_hiragana(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__FIRST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '名前（ひらがな）')
    @saed.declared_attr
    def sex_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), sa.ForeignKey('sexes.sex_id'), nullable = False, server_default = '0', comment = '性別ID')
    @saed.declared_attr
    def birth_day_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.SMALLINT(unsigned = True), sa.ForeignKey('birth_days.birth_day_id'), nullable = False, server_default = '0', comment = '誕生日ID')
    @saed.declared_attr
    def zip_code(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__ZIP_CODE_LENGTH), sa.ForeignKey('zip_addresses.zip_code'), nullable = False, server_default = '', comment = '郵便番号')
    @saed.declared_attr
    def prefecture_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), sa.ForeignKey('zip_addresses.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @saed.declared_attr
    def city_street_address(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__CITY_STREET_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '市区町村・丁目・番地')
    @saed.declared_attr
    def building_room_address(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__BUILDING_ROOM_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '建物名・室名')
    @saed.declared_attr
    def telephone_number(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__TELEPHONE_NUMBER_LENGTH), nullable = False, server_default = '', comment = '電話番号')
    @saed.declared_attr
    def job_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), sa.ForeignKey('jobs.job_id'), nullable = False, server_default = '0', comment = '職業ID')
    @saed.declared_attr
    def job_other(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__JOB_OTHER_LENGTH), nullable = False, server_default = '', comment = '職業その他')
    @saed.declared_attr
    def is_latest_news_hoped(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '最新情報の希望状況')
    @saed.declared_attr
    def file_name(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__FILE_NAME_LENGTH), nullable = False, server_default = '', comment = 'ファイル名')
    @saed.declared_attr
    def file_path(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(users_entity_base.__FILE_PATH_LENGTH), nullable = False, server_default = '', comment = 'ファイルパス')
    @saed.declared_attr
    def remarks(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_blob(), nullable = False, comment = '備考')
    @saed.declared_attr
    def is_personal_information_provide_agreed(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '個人情報提供の同意状況')
    @saed.declared_attr
    def birth_days(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('birth_days_entity', back_populates='users_collection', cascade='merge,save-update', uselist=False)
    @saed.declared_attr
    def jobs(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('jobs_entity', back_populates='users_collection', cascade='merge,save-update', uselist=False)
    @saed.declared_attr
    def sexes(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('sexes_entity', back_populates='users_collection', cascade='merge,save-update', uselist=False)
    @saed.declared_attr
    def user_contact_methods_collection(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('user_contact_methods_entity', back_populates='users', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)
    @saed.declared_attr
    def user_knew_triggers_collection(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('user_knew_triggers_entity', back_populates='users', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)
    @saed.declared_attr
    def zip_addresses(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('zip_addresses_entity', primaryjoin='and_(users_entity.zip_code == zip_addresses_entity.zip_code, users_entity.prefecture_id == zip_addresses_entity.prefecture_id)', back_populates='users_collection', cascade='merge,save-update', uselist=False)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['mail_address', 'token', 'registration_status', 'last_name', 'first_name', 'last_name_hiragana', 'first_name_hiragana', 'sex_id', 'birth_day_id', 'zip_code', 'prefecture_id', 'city_street_address', 'building_room_address', 'telephone_number', 'job_id', 'job_other', 'is_latest_news_hoped', 'file_name', 'file_path', 'remarks', 'is_personal_information_provide_agreed', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['mail_address', 'token', 'registration_status', 'last_name', 'first_name', 'last_name_hiragana', 'first_name_hiragana', 'sex_id', 'birth_day_id', 'zip_code', 'prefecture_id', 'city_street_address', 'building_room_address', 'telephone_number', 'job_id', 'job_other', 'is_latest_news_hoped', 'file_name', 'file_path', 'remarks', 'is_personal_information_provide_agreed', 'updated_at']
