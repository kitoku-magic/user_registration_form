from src.controller.user_registration import *

class user_registration_input_controller(user_registration_common_controller):
    def execute(self):
        # ユーザー登録入力画面を表示する
        self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])

        users_entity_obj = self.get_users_entity()
        if 'previous_page' == users_entity_obj.clicked_button:
            confirm_token = users_entity_obj.token
            users_entity_obj.token = users_entity_obj.input_token
        pre_users_repository_obj = pre_users_repository(pre_users_entity())
        # メールアドレスとトークンが一致して、現在時間が最終更新時間から１時間経っていなければOK
        pre_users_data = pre_users_repository_obj.find(
            ('pre_user_id',),
            'mail_address = %s AND token = %s AND updated_at >= %s',
            (users_entity_obj.mail_address, users_entity_obj.token, (math.floor(time.time()) - 3600))
        )
        if pre_users_data is None:
            raise custom_exception(
                'URLの有効期限が切れています。',
                'URLの有効期限が切れています。\n再度、メールアドレス入力画面からお手続き下さい。'
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
                        raise custom_exception('ファイル情報の更新に失敗しました')
                    self.remove_upload_file(tmp_users_entity_obj)
                users_repository_obj.commit()
            except Exception as exc:
                users_repository_obj.rollback()
                raise custom_exception(
                    str(exc),
                    'システムエラーが発生しました。\n再度、ユーザー登録入力画面から操作をお願いします。'
                )
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
        # フォームの初期値を設定する為の初期化
        self.assign_all_form_data()
        # 複数選択項目の表示内容を取得して設定
        self.set_multiple_value_item()
        # 複数選択項目の選択状態を設定
        self.select_multiple_value_item()

        self.set_template_file_name('user_registration/input')
