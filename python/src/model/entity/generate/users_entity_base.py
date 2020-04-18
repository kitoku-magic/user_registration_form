from src.database import db
from src.model.entity import declared_attr, entity, BIGINT, my_varbinary, TINYINT, SMALLINT, my_blob, timestamp_mixin_entity
from src.model.entity.generate import Column, List, Type, TypeVar, RelationshipProperty

T = TypeVar('T', bound='users_entity_base')

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

    def get_mail_address_length(cls: Type[T]) -> int:
        return users_entity_base.__MAIL_ADDRESS_LENGTH
    def get_token_length(cls: Type[T]) -> int:
        return users_entity_base.__TOKEN_LENGTH
    def get_last_name_length(cls: Type[T]) -> int:
        return users_entity_base.__LAST_NAME_LENGTH
    def get_first_name_length(cls: Type[T]) -> int:
        return users_entity_base.__FIRST_NAME_LENGTH
    def get_last_name_hiragana_length(cls: Type[T]) -> int:
        return users_entity_base.__LAST_NAME_HIRAGANA_LENGTH
    def get_first_name_hiragana_length(cls: Type[T]) -> int:
        return users_entity_base.__FIRST_NAME_HIRAGANA_LENGTH
    def get_zip_code_length(cls: Type[T]) -> int:
        return users_entity_base.__ZIP_CODE_LENGTH
    def get_city_street_address_length(cls: Type[T]) -> int:
        return users_entity_base.__CITY_STREET_ADDRESS_LENGTH
    def get_building_room_address_length(cls: Type[T]) -> int:
        return users_entity_base.__BUILDING_ROOM_ADDRESS_LENGTH
    def get_telephone_number_length(cls: Type[T]) -> int:
        return users_entity_base.__TELEPHONE_NUMBER_LENGTH
    def get_job_other_length(cls: Type[T]) -> int:
        return users_entity_base.__JOB_OTHER_LENGTH
    def get_file_name_length(cls: Type[T]) -> int:
        return users_entity_base.__FILE_NAME_LENGTH
    def get_file_path_length(cls: Type[T]) -> int:
        return users_entity_base.__FILE_PATH_LENGTH

    @declared_attr
    def user_id(cls: Type[T]) -> Column:
        return db.Column(BIGINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = 'ユーザーID')
    @declared_attr
    def mail_address(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__MAIL_ADDRESS_LENGTH), nullable = False, server_default = '', comment = 'メールアドレス')
    @declared_attr
    def token(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__TOKEN_LENGTH), nullable = False, server_default = '', comment = 'トークン値')
    @declared_attr
    def registration_status(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '登録状況')
    @declared_attr
    def last_name(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__LAST_NAME_LENGTH), nullable = False, server_default = '', comment = '苗字')
    @declared_attr
    def first_name(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__FIRST_NAME_LENGTH), nullable = False, server_default = '', comment = '名前')
    @declared_attr
    def last_name_hiragana(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__LAST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '苗字（ひらがな）')
    @declared_attr
    def first_name_hiragana(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__FIRST_NAME_HIRAGANA_LENGTH), nullable = False, server_default = '', comment = '名前（ひらがな）')
    @declared_attr
    def sex_id(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), db.ForeignKey('sexes.sex_id'), nullable = False, server_default = '0', comment = '性別ID')
    @declared_attr
    def birth_day_id(cls: Type[T]) -> Column:
        return db.Column(SMALLINT(unsigned = True), db.ForeignKey('birth_days.birth_day_id'), nullable = False, server_default = '0', comment = '誕生日ID')
    @declared_attr
    def zip_code(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__ZIP_CODE_LENGTH), db.ForeignKey('zip_addresses.zip_code'), nullable = False, server_default = '', comment = '郵便番号')
    @declared_attr
    def prefecture_id(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), db.ForeignKey('zip_addresses.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @declared_attr
    def city_street_address(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__CITY_STREET_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '市区町村・丁目・番地')
    @declared_attr
    def building_room_address(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__BUILDING_ROOM_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '建物名・室名')
    @declared_attr
    def telephone_number(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__TELEPHONE_NUMBER_LENGTH), nullable = False, server_default = '', comment = '電話番号')
    @declared_attr
    def job_id(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), db.ForeignKey('jobs.job_id'), nullable = False, server_default = '0', comment = '職業ID')
    @declared_attr
    def job_other(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__JOB_OTHER_LENGTH), nullable = False, server_default = '', comment = '職業その他')
    @declared_attr
    def is_latest_news_hoped(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '最新情報の希望状況')
    @declared_attr
    def file_name(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__FILE_NAME_LENGTH), nullable = False, server_default = '', comment = 'ファイル名')
    @declared_attr
    def file_path(cls: Type[T]) -> Column:
        return db.Column(my_varbinary(users_entity_base.__FILE_PATH_LENGTH), nullable = False, server_default = '', comment = 'ファイルパス')
    @declared_attr
    def remarks(cls: Type[T]) -> Column:
        return db.Column(my_blob(), nullable = False, comment = '備考')
    @declared_attr
    def is_personal_information_provide_agreed(cls: Type[T]) -> Column:
        return db.Column(TINYINT(unsigned = True), nullable = False, server_default = '0', comment = '個人情報提供の同意状況')
    @declared_attr
    def birth_days(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('birth_days_entity', back_populates='users_collection', cascade='merge,save-update', uselist=False)
    @declared_attr
    def jobs(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('jobs_entity', back_populates='users_collection', cascade='merge,save-update', uselist=False)
    @declared_attr
    def sexes(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('sexes_entity', back_populates='users_collection', cascade='merge,save-update', uselist=False)
    @declared_attr
    def user_contact_methods_collection(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('user_contact_methods_entity', back_populates='users', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)
    @declared_attr
    def user_knew_triggers_collection(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('user_knew_triggers_entity', back_populates='users', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)
    @declared_attr
    def zip_addresses(cls: Type[T]) -> RelationshipProperty:
        return db.relationship('zip_addresses_entity', primaryjoin='and_(users_entity.zip_code == zip_addresses_entity.zip_code, users_entity.prefecture_id == zip_addresses_entity.prefecture_id)', back_populates='users_collection', cascade='merge,save-update', uselist=False)

    def __init__(self: Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: Type[T]) -> List[str]:
        return ['mail_address', 'token', 'registration_status', 'last_name', 'first_name', 'last_name_hiragana', 'first_name_hiragana', 'sex_id', 'birth_day_id', 'zip_code', 'prefecture_id', 'city_street_address', 'building_room_address', 'telephone_number', 'job_id', 'job_other', 'is_latest_news_hoped', 'file_name', 'file_path', 'remarks', 'is_personal_information_provide_agreed', 'created_at', 'updated_at']
    def get_update_column_name_list(self: Type[T]) -> List[str]:
        return ['mail_address', 'token', 'registration_status', 'last_name', 'first_name', 'last_name_hiragana', 'first_name_hiragana', 'sex_id', 'birth_day_id', 'zip_code', 'prefecture_id', 'city_street_address', 'building_room_address', 'telephone_number', 'job_id', 'job_other', 'is_latest_news_hoped', 'file_name', 'file_path', 'remarks', 'is_personal_information_provide_agreed', 'updated_at']
