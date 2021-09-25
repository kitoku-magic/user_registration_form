from src import typing
from src.model.entity.generate.pre_users_entity_base import pre_users_entity_base

T = typing.TypeVar('T', bound='pre_users_entity')

class pre_users_entity(pre_users_entity_base):
    """
    ユーザー事前登録情報テーブルのエンティティクラス
    """
    def __init__(self: typing.Type[T]) -> None:
        super().__init__()
    def set_validation_setting(self: typing.Type[T]):
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
        ]

        for validation_setting in validation_settings:
            self.add_validation_settings(
                validation_setting['name'],
                validation_setting['show_name'],
                validation_setting['rules']
            )
