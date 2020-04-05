from src.controller.user_registration import *

class user_registration_complete_controller(user_registration_common_controller):
    def execute(self):
        users_entity_obj = self.get_users_entity()
        if 'next_page' != users_entity_obj.clicked_button:
            raise custom_exception(setting.app.config['INVALID_REQUEST_ERROR'])
        is_file_delete = False
        users_repository_obj = users_repository(users_entity_obj)
        users_repository_obj.begin()
        try:
            pre_users_entity_obj = pre_users_entity()
            get_pre_user_column_name_list = pre_users_entity_obj.get_update_column_name_list()
            pre_users_repository_obj = pre_users_repository(pre_users_entity_obj)
            pre_users_data = pre_users_repository_obj.find(
                get_pre_user_column_name_list,
                'mail_address = %s AND token = %s',
                (users_entity_obj.mail_address, users_entity_obj.input_token),
                '',
                True
            )
            if pre_users_data is None:
                raise custom_exception(setting.app.config['PRE_USER_NOT_EXIST_ERROR'])
            row_count = pre_users_repository_obj.delete(
                'mail_address = %s AND token = %s',
                (users_entity_obj.mail_address, users_entity_obj.input_token)
            )
            if 0 >= row_count:
                raise custom_exception(
                    setting.app.config['PRE_USER_DELETE_ERROR']
                )
            get_column_name_list = users_entity_obj.get_update_column_name_list()
            get_column_name_list.insert(0, 'user_id')
            users_data = users_repository_obj.find(
                get_column_name_list,
                'mail_address = %s AND token = %s',
                (users_entity_obj.mail_address, users_entity_obj.token),
                '',
                True
            )
            if users_data is None:
                raise custom_exception(setting.app.config['USER_NOT_EXIST_ERROR'])
            for index, value in enumerate(get_column_name_list):
                setattr(users_entity_obj, value, users_data[index])
            old_file_path = users_entity_obj.file_path
            if False == util.is_empty(users_entity_obj.file_path):
                users_entity_obj.file_path = users_entity_obj.file_path.replace(
                    setting.app.config['APP_FILE_TMP_SAVE_PATH'],
                    setting.app.config['APP_FILE_SAVE_PATH']
                )
                is_file_delete = True
            users_entity_obj.registration_status = setting.app.config['USER_REGISTRATION_STATUS_REGISTERED']
            users_entity_obj.token = util.get_token_for_url(setting.app.config['SECRET_TOKEN_FOR_URL_BYTE_LENGTH'])
            update_column_name_list = users_entity_obj.get_update_column_name_list()
            row_count = users_repository_obj.update(
                user_contact_methods_entity(),
                user_knew_triggers_entity(),
                update_column_name_list,
                'user_id = %s',
                (users_entity_obj.user_id,)
            )
            if 1 > row_count:
                raise custom_exception(setting.app.config['USER_SAVE_ERROR'])
            if False == util.is_empty(old_file_path):
                new_dir = os.path.dirname(users_entity_obj.file_path)
                r = util.make_directory(new_dir)
                if False == r:
                    raise custom_exception(setting.app.config['UPLOAD_FILE_SAVE_DIRECTORY_MAKE_ERROR'])
                os.chmod(new_dir, 0o700)
                os.rename(old_file_path, users_entity_obj.file_path)
                os.chmod(users_entity_obj.file_path, 0o600)
            users_repository_obj.commit()
        except Exception as exc:
            users_repository_obj.rollback()
            if True == is_file_delete:
                self.remove_upload_file(users_entity_obj)
                if False == util.is_empty(old_file_path) and os.path.isfile(old_file_path):
                    os.remove(old_file_path)
            raise custom_exception(
                str(exc),
                setting.app.config['SHOW_USER_REGISTRATION_ERROR']
            )
        # ユーザー登録完了画面を表示する
        self.set_template_common_data(setting.app.config['USER_REGISTRATION_COMPLETE_TITLE'], 'user_registration/complete')
