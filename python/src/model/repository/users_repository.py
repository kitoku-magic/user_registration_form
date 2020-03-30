from src.model.repository import *

class users_repository(repository):
    def __init__(self, users_entity):
        super().__init__(users_entity)
    def insert(self, columns):
        row_count = super().insert(columns)
        if 0 >= row_count:
            return row_count
        main_entity = self.get_main_entity()
        user_id = self.last_insert_id()
        for user_contact_methods_entity_obj in main_entity.user_contact_methods_collection:
            user_contact_methods_entity_obj.user_id = user_id
            user_contact_methods_entity_obj.contact_method_id = int(user_contact_methods_entity_obj.contact_method_id)
        row_count = super().bulk_insert(main_entity.user_contact_methods_collection)
        if 0 >= row_count:
            return row_count
        for user_knew_triggers_entity_obj in main_entity.user_knew_triggers_collection:
            user_knew_triggers_entity_obj.user_id = user_id
            user_knew_triggers_entity_obj.knew_trigger_id = int(user_knew_triggers_entity_obj.knew_trigger_id)
        row_count = super().bulk_insert(main_entity.user_knew_triggers_collection)
        return row_count
    def update(self, user_contact_methods_entity_obj, user_knew_triggers_entity_obj, columns, where = '', params = ()):
        row_count = super().update(columns, where, params)
        if 0 >= row_count:
            return row_count
        main_entity = self.get_main_entity()
        if 0 < len(main_entity.user_contact_methods_collection):
            user_contact_methods_repository_obj = user_contact_methods_repository(user_contact_methods_entity_obj)
            row_count = user_contact_methods_repository_obj.delete(
                'user_id = %s',
                (main_entity.user_id,)
            )
            if 0 >= row_count:
                return row_count
            for user_contact_methods_entity in main_entity.user_contact_methods_collection:
                user_contact_methods_entity.user_id = main_entity.user_id
                user_contact_methods_entity.contact_method_id = int(user_contact_methods_entity.contact_method_id)
            row_count = super().bulk_insert(main_entity.user_contact_methods_collection)
            if 0 >= row_count:
                return row_count
        if 0 < len(main_entity.user_knew_triggers_collection):
            user_knew_triggers_repository_obj = user_knew_triggers_repository(user_knew_triggers_entity_obj)
            row_count = user_knew_triggers_repository_obj.delete(
                'user_id = %s',
                (main_entity.user_id,)
            )
            if 0 >= row_count:
                return row_count
            for user_knew_triggers_entity in main_entity.user_knew_triggers_collection:
                user_knew_triggers_entity.user_id = main_entity.user_id
                user_knew_triggers_entity.knew_trigger_id = int(user_knew_triggers_entity.knew_trigger_id)
            row_count = super().bulk_insert(main_entity.user_knew_triggers_collection)
        return row_count
