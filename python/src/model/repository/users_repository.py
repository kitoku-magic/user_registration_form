from python_library.src.custom_sqlalchemy.repository import repository
from src import collections
from src import typing
from src.model.entity.users_entity import users_entity
from src.model.entity.user_contact_methods_entity import user_contact_methods_entity
from src.model.entity.user_knew_triggers_entity import user_knew_triggers_entity

T = typing.TypeVar('T', bound='users_repository')

class users_repository(repository):
    """
    ユーザーテーブルのリポジトリクラス
    """
    def __init__(self: typing.Type[T], users_entity: users_entity) -> None:
        super().__init__(users_entity)
    def insert(self: typing.Type[T], target_column_name_list):

        """
        INSERT文を実行する（データが存在していれば関連テーブルも）
        """
        # 途中で処理が終わるのを考慮し、main_entity_classを状況に応じて切り替えている
        entity = self.get_main_entity()
        row_count = super().insert([entity], target_column_name_list)
        if 0 >= row_count:
            return row_count
        user_id = self.last_insert_id()
        target_column_name_list = []
        for user_contact_methods_entity_obj in entity.user_contact_methods_collection:
            target_column_name_list = user_contact_methods_entity_obj.get_insert_column_name_list()
            user_contact_methods_entity_obj.user_id = user_id
            user_contact_methods_entity_obj.contact_method_id = int(user_contact_methods_entity_obj.contact_method_id)
        self.set_main_entity_class(user_contact_methods_entity)
        row_count = super().insert(entity.user_contact_methods_collection, target_column_name_list)
        self.set_main_entity_class(users_entity)
        if 0 >= row_count:
            return row_count
        target_column_name_list = []
        for user_knew_triggers_entity_obj in entity.user_knew_triggers_collection:
            target_column_name_list = user_knew_triggers_entity_obj.get_insert_column_name_list()
            user_knew_triggers_entity_obj.user_id = user_id
            user_knew_triggers_entity_obj.knew_trigger_id = int(user_knew_triggers_entity_obj.knew_trigger_id)
        self.set_main_entity_class(user_knew_triggers_entity)
        row_count = super().insert(entity.user_knew_triggers_collection, target_column_name_list)
        self.set_main_entity_class(users_entity)
        return row_count
    def update(self: typing.Type[T], target_column_name_list, where = '', params = {}):
        """
        UPDATE文を実行する（データが存在していれば関連テーブルも）
        """
        # 途中で処理が終わるのを考慮し、main_entity_classを状況に応じて切り替えている
        main_entity = self.get_main_entity()
        row_count = super().update(target_column_name_list, where, params)
        if 0 >= row_count:
            return row_count
        # DELETE → INSERTではなく、データの存在状況によって、INSERT・UPDATE・DELETEを使い分けた方が高速？
        if 0 < len(main_entity.user_contact_methods_collection):
            self.set_main_entity_class(user_contact_methods_entity)
            row_count = super().delete(
                'user_id = :user_id',
                collections.OrderedDict(
                    user_id = main_entity.user_id
                )
            )
            self.set_main_entity_class(users_entity)
            if 0 >= row_count:
                return row_count
            target_column_name_list = []
            for user_contact_methods_entity_obj in main_entity.user_contact_methods_collection:
                target_column_name_list = user_contact_methods_entity_obj.get_insert_column_name_list()
                user_contact_methods_entity_obj.user_id = main_entity.user_id
                user_contact_methods_entity_obj.contact_method_id = int(user_contact_methods_entity_obj.contact_method_id)
            self.set_main_entity_class(user_contact_methods_entity)
            row_count = super().insert(main_entity.user_contact_methods_collection, target_column_name_list)
            self.set_main_entity_class(users_entity)
            if 0 >= row_count:
                return row_count
        if 0 < len(main_entity.user_knew_triggers_collection):
            self.set_main_entity_class(user_knew_triggers_entity)
            row_count = super().delete(
                'user_id = :user_id',
                collections.OrderedDict(
                    user_id = main_entity.user_id
                )
            )
            self.set_main_entity_class(users_entity)
            if 0 >= row_count:
                return row_count
            target_column_name_list = []
            for user_knew_triggers_entity_obj in main_entity.user_knew_triggers_collection:
                target_column_name_list = user_knew_triggers_entity_obj.get_insert_column_name_list()
                user_knew_triggers_entity_obj.user_id = main_entity.user_id
                user_knew_triggers_entity_obj.knew_trigger_id = int(user_knew_triggers_entity_obj.knew_trigger_id)
            self.set_main_entity_class(user_knew_triggers_entity)
            row_count = super().insert(main_entity.user_knew_triggers_collection, target_column_name_list)
            self.set_main_entity_class(users_entity)
        return row_count
