from python_library.src.original.custom_exception import custom_exception
from python_library.src.original.util import util
from src import collections
from src import os
from src.application import app
from src.controller.user_registration.user_registration_common_controller import user_registration_common_controller
from src.model.entity.pre_users_entity import pre_users_entity
from src.model.entity.users_entity import users_entity
from src.model.repository.pre_users_repository import pre_users_repository
from src.model.repository.users_repository import users_repository

class user_registration_complete_controller(user_registration_common_controller):
    """
    ユーザー登録の入力完了処理
    """
    def execute(self):
        users_entity_obj = self.get_users_entity()
        if 'next_page' != users_entity_obj.clicked_button:
            raise custom_exception(app.config['INVALID_REQUEST_ERROR'])
        is_file_delete = False
        users_repository_obj = users_repository(users_entity_obj)
        users_repository_obj.begin()
        try:
            pre_users_repository_obj = pre_users_repository(pre_users_entity())
            pre_users_data = pre_users_repository_obj.find(
                (pre_users_entity.pre_user_id,),
                'mail_address = :mail_address AND token = :token',
                collections.OrderedDict(
                    mail_address = users_entity_obj.mail_address,
                    token = users_entity_obj.input_token
                ),
                '',
                True
            )
            # ユーザーの事前登録のレコードが無い場合はエラー
            if pre_users_data is None:
                raise custom_exception(app.config['PRE_USER_NOT_EXIST_ERROR'])
            row_count = pre_users_repository_obj.delete(
                'mail_address = :mail_address AND token = :token',
                collections.OrderedDict(
                    mail_address = users_entity_obj.mail_address,
                    token = users_entity_obj.input_token
                )
            )
            if 0 >= row_count:
                raise custom_exception(
                    app.config['PRE_USER_DELETE_ERROR']
                )
            users_data = users_repository_obj.find(
                (users_entity,),
                'mail_address = :mail_address AND token = :token',
                collections.OrderedDict(
                    mail_address = users_entity_obj.mail_address,
                    token = users_entity_obj.token
                ),
                '',
                True
            )
            # ユーザー登録のレコードが無い場合もエラー
            if users_data is None:
                raise custom_exception(app.config['USER_NOT_EXIST_ERROR'])
            get_column_name_list = users_entity_obj.get_update_column_name_list()
            get_column_name_list.insert(0, 'user_id')
            for column_name in get_column_name_list:
                setattr(users_entity_obj, column_name, getattr(users_data, column_name))
            old_file_path = users_entity_obj.file_path
            if False == util.is_empty(users_entity_obj.file_path):
                # 添付ファイルが存在する場合は、ファイルパスの内容を正式な場所に変更する
                users_entity_obj.file_path = users_entity_obj.file_path.replace(
                    app.config['APP_FILE_TMP_SAVE_PATH'],
                    app.config['APP_FILE_SAVE_PATH']
                )
                is_file_delete = True
            users_entity_obj.registration_status = app.config['USER_REGISTRATION_STATUS_REGISTERED']
            users_entity_obj.token = util.get_token_for_url(app.config['SECRET_TOKEN_FOR_URL_BYTE_LENGTH'])
            row_count = users_repository_obj.update(
                users_entity_obj.get_update_column_name_list(),
                'user_id = :b_user_id',
                collections.OrderedDict(
                    b_user_id = users_entity_obj.user_id
                )
            )
            if 1 > row_count:
                raise custom_exception(app.config['USER_SAVE_ERROR'])
            if False == util.is_empty(old_file_path):
                # 添付ファイルが存在する場合は、ファイルの置き場所を移動する
                new_dir = os.path.dirname(users_entity_obj.file_path)
                r = util.make_directory(new_dir)
                if False == r:
                    raise custom_exception(app.config['UPLOAD_FILE_SAVE_DIRECTORY_MAKE_ERROR'])
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
                app.config['SHOW_USER_REGISTRATION_ERROR']
            )
        # ユーザー登録完了画面を表示する
        self.set_template_common_data(app.config['USER_REGISTRATION_COMPLETE_TITLE'], 'user_registration/complete')
