from src.controller.user_registration import *

class user_registration_input_controller(user_registration_common_controller):
    """
    ユーザー登録の入力処理
    """
    def execute(self):
        users_entity_obj = self.get_users_entity()
        if 'previous_page' == users_entity_obj.clicked_button:
            # 確認画面用のトークンは、ユーザーデータの再取得に使う
            confirm_token = users_entity_obj.token
            users_entity_obj.token = users_entity_obj.input_token
        pre_users_repository_obj = pre_users_repository(pre_users_entity())
        # メールアドレスとトークンが一致して、現在時間が最終更新時間からUSER_REGISTRATION_TIME_LIMIT_SECOND秒経っていなければOK
        pre_users_data = pre_users_repository_obj.find(
            ('pre_user_id',),
            'mail_address = %s AND token = %s AND updated_at >= %s',
            (users_entity_obj.mail_address, users_entity_obj.token, (math.floor(time.time()) - setting.app.config['USER_REGISTRATION_TIME_LIMIT_SECOND']))
        )
        if pre_users_data is None:
            raise custom_exception(
                setting.app.config['USER_REGISTRATION_URL_EXPIRE_DATE_ERROR'],
                setting.app.config['SHOW_USER_REGISTRATION_URL_EXPIRE_DATE_ERROR']
            )
        if 'previous_page' == users_entity_obj.clicked_button:
            get_column_name_list = users_entity_obj.get_update_column_name_list()
            # tokenは、pre_usersテーブルのtoken(input_token)を使うので、取得して更新する必要はない
            get_column_name_list.remove('token')
            get_column_name_list.insert(0, 'user_id')
            users_repository_obj = users_repository(users_entity_obj)
            users_repository_obj.begin()
            users_data = None
            try:
                # 確認画面で設定されたデータの取得
                users_data = users_repository_obj.find(
                    get_column_name_list,
                    'mail_address = %s AND token = %s',
                    (users_entity_obj.mail_address, confirm_token),
                    '',
                    True
                )
                if users_data is not None:
                    for index, value in enumerate(get_column_name_list):
                        setattr(users_entity_obj, value, users_data[index])
                    # アップロードされたファイルの削除と、DB内のファイル情報の初期化
                    tmp_users_entity_obj = users_entity()
                    tmp_users_entity_obj.file_name = users_entity_obj.file_name
                    tmp_users_entity_obj.file_path = users_entity_obj.file_path
                    users_entity_obj.file_name = ''
                    users_entity_obj.file_path = ''
                    row_count = users_repository_obj.update(
                        user_contact_methods_entity(),
                        user_knew_triggers_entity(),
                        ['file_name', 'file_path'],
                        'user_id = %s',
                        (users_entity_obj.user_id,)
                    )
                    if 1 > row_count:
                        raise custom_exception(setting.app.config['FILE_UPDATE_ERROR'])
                    self.remove_upload_file(tmp_users_entity_obj)
                users_repository_obj.commit()
            except Exception as exc:
                users_repository_obj.rollback()
                raise custom_exception(
                    str(exc),
                    setting.app.config['SHOW_SYSTEM_ERROR']
                )
            # 以下は、特殊なケースの項目
            # 誕生日
            birth_days_entity_obj = birth_days_entity()
            get_column_name_list = birth_days_entity_obj.get_update_column_name_list()
            birth_days_repository_obj = birth_days_repository(birth_days_entity_obj)
            birth_days_data = birth_days_repository_obj.find(
                ('birth_day',),
                'birth_day_id = %s',
                (users_entity_obj.birth_day_id,)
            )
            if birth_days_data is not None:
                users_entity_obj.birth_year = birth_days_data[0].year
                users_entity_obj.birth_month = birth_days_data[0].month
                users_entity_obj.birth_day = birth_days_data[0].day
            # 連絡方法
            user_contact_methods_entity_obj = user_contact_methods_entity()
            get_column_name_list = user_contact_methods_entity_obj.get_update_column_name_list()
            user_contact_methods_repository_obj = user_contact_methods_repository(user_contact_methods_entity_obj)
            user_contact_methods_data_list = user_contact_methods_repository_obj.find_all(
                ('contact_method_id',),
                'user_id = %s',
                (users_entity_obj.user_id,)
            )
            if 0 < len(user_contact_methods_data_list):
                for user_contact_methods_data in user_contact_methods_data_list:
                    user_contact_methods_entity_obj = user_contact_methods_entity()
                    user_contact_methods_entity_obj.contact_method_id = user_contact_methods_data[0]
                    users_entity_obj.user_contact_methods_collection.append(user_contact_methods_entity_obj)
            # 知ったきっかけ
            user_knew_triggers_entity_obj = user_knew_triggers_entity()
            get_column_name_list = user_knew_triggers_entity_obj.get_update_column_name_list()
            user_knew_triggers_repository_obj = user_knew_triggers_repository(user_knew_triggers_entity_obj)
            user_knew_triggers_data_list = user_knew_triggers_repository_obj.find_all(
                ('knew_trigger_id',),
                'user_id = %s',
                (users_entity_obj.user_id,)
            )
            if 0 < len(user_knew_triggers_data_list):
                for user_knew_triggers_data in user_knew_triggers_data_list:
                    user_knew_triggers_entity_obj = user_knew_triggers_entity()
                    user_knew_triggers_entity_obj.knew_trigger_id = user_knew_triggers_data[0]
                    users_entity_obj.user_knew_triggers_collection.append(user_knew_triggers_entity_obj)
        # 全てのフォーム項目に値を設定する
        self.assign_all_form_data()
        # 選択項目の表示内容を取得して設定
        self.set_value_item()
        # 選択項目の選択状態を設定
        self.select_value_item()

        # ユーザー登録入力画面を表示する
        self.set_template_common_data(setting.app.config['USER_REGISTRATION_INPUT_TITLE'], 'user_registration/input')
