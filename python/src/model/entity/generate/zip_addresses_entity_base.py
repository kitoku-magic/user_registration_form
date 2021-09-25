from src import typing
from python_library.src import sa
from python_library.src import sadm
from python_library.src import saed
from python_library.src import sao
from python_library.src import saor
from python_library.src import sassc
from python_library.src.custom_sqlalchemy.custom_varbinary import custom_varbinary
from python_library.src.custom_sqlalchemy.entity import entity
from python_library.src.custom_sqlalchemy.timestamp_mixin_entity import timestamp_mixin_entity

T = typing.TypeVar('T', bound='zip_addresses_entity_base')

class zip_addresses_entity_base(timestamp_mixin_entity, entity):
    """
    郵便番号住所マスタテーブルエンティティの基底クラス
    """
    __abstract__: bool = True
    __ZIP_CODE_LENGTH: int = 7
    __CITY_DISTRICT_COUNTY_LENGTH: int = 64
    __TOWN_VILLAGE_ADDRESS_LENGTH: int = 128

    def get_zip_code_length(cls: typing.Type[T]) -> int:
        return zip_addresses_entity_base.__ZIP_CODE_LENGTH
    def get_city_district_county_length(cls: typing.Type[T]) -> int:
        return zip_addresses_entity_base.__CITY_DISTRICT_COUNTY_LENGTH
    def get_town_village_address_length(cls: typing.Type[T]) -> int:
        return zip_addresses_entity_base.__TOWN_VILLAGE_ADDRESS_LENGTH

    @saed.declared_attr
    def zip_address_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.MEDIUMINT(unsigned = True), nullable = False, autoincrement = True, primary_key = True, comment = '郵便番号住所ID')
    @saed.declared_attr
    def zip_code(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(zip_addresses_entity_base.__ZIP_CODE_LENGTH), nullable = False, server_default = '', comment = '郵便番号')
    @saed.declared_attr
    def prefecture_id(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(sadm.TINYINT(unsigned = True), sa.ForeignKey('prefectures.prefecture_id'), nullable = False, server_default = '0', comment = '都道府県ID')
    @saed.declared_attr
    def city_district_county(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(zip_addresses_entity_base.__CITY_DISTRICT_COUNTY_LENGTH), nullable = False, server_default = '', comment = '市区群')
    @saed.declared_attr
    def town_village_address(cls: typing.Type[T]) -> sassc.Column:
        return sassc.Column(custom_varbinary(zip_addresses_entity_base.__TOWN_VILLAGE_ADDRESS_LENGTH), nullable = False, server_default = '', comment = '町村番地')
    @saed.declared_attr
    def prefectures(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('prefectures_entity', back_populates='zip_addresses_collection', cascade='merge,save-update', uselist=False)
    @saed.declared_attr
    def users_collection(cls: typing.Type[T]) -> saor.RelationshipProperty:
        return sao.relationship('users_entity', primaryjoin='and_(zip_addresses_entity.zip_code == users_entity.zip_code, zip_addresses_entity.prefecture_id == users_entity.prefecture_id)', back_populates='zip_addresses', cascade='delete,delete-orphan,expunge,merge,refresh-expire,save-update', uselist=True)

    def __init__(self: typing.Type[T]) -> None:
        timestamp_mixin_entity.__init__(self)
    def set_validation_setting(self: typing.Type[T]) -> None:
        pass
    def get_insert_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['zip_code', 'prefecture_id', 'city_district_county', 'town_village_address', 'created_at', 'updated_at']
    def get_update_column_name_list(self: typing.Type[T]) -> typing.List[str]:
        return ['zip_code', 'prefecture_id', 'city_district_county', 'town_village_address', 'updated_at']
