from src.controller.user_registration import *

class user_registration_confirm_controller(user_registration_common_controller):
    def execute(self):
        request = self.get_request()
        request_form = request.form
        request_files = request.files
        users_entity_obj = self.get_users_entity()
        for contact_method in request_form.getlist('contact_method'):
            user_contact_methods_entity_obj = user_contact_methods_entity()
            user_contact_methods_entity_obj.contact_method_id = contact_method
            users_entity_obj.user_contact_methods_collection.append(user_contact_methods_entity_obj)
        for knew_trigger in request_form.getlist('knew_trigger'):
            user_knew_triggers_entity_obj = user_knew_triggers_entity()
            user_knew_triggers_entity_obj.knew_trigger_id = knew_trigger
            users_entity_obj.user_knew_triggers_collection.append(user_knew_triggers_entity_obj)
        users_entity_obj.file_name = request_files.getlist('file_name')
        users_entity_obj.trim_all_data()
        properties = users_entity_obj.get_all_properties()
        for field, value in properties.items():
            if 'last_name' == field or 'first_name' == field:
                value = jaconv.h2z(str(value))
                value = util.join_diacritic(value)
            elif 'last_name_hiragana' == field or 'first_name_hiragana' == field:
                value = jaconv.kata2hira(jaconv.h2z(str(value)))
                value = util.join_diacritic(value)
            elif 'zip_code' == field or 'telephone_number' == field:
                value = jaconv.z2h(str(value), digit=True)
                value = util.replace_hyphen(value, '-')
            elif 'city_street_address' == field or 'building_room_address' == field or 'job_other' == field:
                value = jaconv.h2z(str(value), kana=True, digit=True, ascii=True)
                value = util.replace_hyphen(value, 'ー')
            setattr(users_entity_obj, field, value)

        birth_year = users_entity_obj.birth_year
        birth_month = users_entity_obj.birth_month
        birth_day = users_entity_obj.birth_day
        if True == util.is_empty(birth_year) and True == util.is_empty(birth_month) and True == util.is_empty(birth_day):
            users_entity_obj.birth_day_full = None
        else:
            users_entity_obj.birth_day_full = str(birth_year) + '-' + str(birth_month).zfill(2) + '-' + str(birth_day).zfill(2)

        zip_codes = users_entity_obj.zip_code.split('-')
        if 2 > len(zip_codes):
            zip_codes = ['', '']

        # 郵便番号から住所情報を取得
        zip_addresses_repository_obj = zip_addresses_repository(zip_addresses_entity())
        street_address_data = zip_addresses_repository_obj.find(
            ('zip_address_id', 'prefecture_id', 'city_district_county', 'town_village_address'),
            'zip_code = %s',
            (zip_codes[0] + zip_codes[1],)
        )
        if 'street_address_search' == users_entity_obj.clicked_button:
            is_next_page_forward = False
            if street_address_data is None:
                users_entity_obj.zip_code_error = setting.app.config['ZIP_CODE_ERROR']
                users_entity_obj.prefecture_id = ''
                users_entity_obj.city_street_address = ''
            else:
                users_entity_obj.prefecture_id = street_address_data[1]
                users_entity_obj.city_street_address = street_address_data[2] + street_address_data[3]
        elif 'next_page' == users_entity_obj.clicked_button:
            is_next_page_forward = True
            users_entity_obj.set_validation_setting();
            is_next_page_forward = users_entity_obj.validate();
            # 郵便番号の存在結果
            if users_entity_obj.zip_code_error is None and street_address_data is None:
                is_next_page_forward = False;
                users_entity_obj.zip_code_error = setting.app.config['ZIP_CODE_ERROR']
                users_entity_obj.prefecture_id = ''
                users_entity_obj.city_street_address = ''
        else:
            raise custom_exception('不正なリクエストです')

        if True == is_next_page_forward:
            # データの存在チェック
            # ユーザー登録済みチェック
            is_user_exist = True
            users_repository_obj = users_repository(users_entity_obj)
            users_data = users_repository_obj.find(
                    ('user_id','registration_status'),
                    'mail_address = %s',
                    (users_entity_obj.mail_address,)
            )
            if users_data is None:
                is_user_exist = False
            else:
                if setting.app.config['USER_REGISTRATION_STATUS_REGISTERED'] != users_data[1]:
                    is_user_exist = False
                    users_entity_obj.user_id = users_data[0]
            if True == is_user_exist:
                is_next_page_forward = False
                users_entity_obj.mail_address_error = '既に該当のメールアドレスでは登録済みです。'
            # 誕生日存在チェック
            birth_days_repository_obj = birth_days_repository(birth_days_entity())
            birth_days_data = birth_days_repository_obj.find(
                ('birth_day_id',),
                'birth_day = %s',
                (users_entity_obj.birth_day_full,)
            )
            if birth_days_data is None:
                is_next_page_forward = False
                users_entity_obj.birth_day_full_error = '登録出来ない誕生日です。'
            else:
                users_entity_obj.birth_day_id = birth_days_data[0]

        if True == is_next_page_forward:
            if users_entity_obj.file_path is None:
                users_entity_obj.file_name = ''
                users_entity_obj.file_path = ''
            if setting.app.config['JOB_ID_OTHER'] != users_entity_obj.job_id:
                users_entity_obj.job_other = ''
            users_entity_obj.previous_token = users_entity_obj.token
            users_entity_obj.token = util.get_token_for_url(96)
            users_entity_obj.registration_status = setting.app.config['USER_REGISTRATION_STATUS_REGISTERING']
            users_entity_obj.zip_code = zip_codes[0] + zip_codes[1]
            update_column_name_list = users_entity_obj.get_update_column_name_list()
            users_repository_obj.begin()
            try:
                if users_entity_obj.user_id is None:
                    row_count = users_repository_obj.insert(update_column_name_list)
                else:
                    row_count = users_repository_obj.update(
                        user_contact_methods_entity(),
                        user_knew_triggers_entity(),
                        update_column_name_list,
                        'user_id = %s',
                        (users_entity_obj.user_id,)
                    )
                if 1 > row_count:
                    raise custom_exception('ユーザー情報の一時保存に失敗しました')
                users_repository_obj.commit()
            except Exception as exc:
                users_repository_obj.rollback()
                self.remove_upload_file(users_entity_obj)
                raise custom_exception(
                    str(exc),
                    'システムエラーが発生しました。\n再度、ユーザー登録入力画面から操作をお願いします。'
                )
            # ユーザー登録確認画面を表示する
            self.add_response_data('title', setting.app.config['USER_REGISTRATION_CONFIRM_TITLE'])
            self.set_template_file_name('user_registration/confirm')
        else:
            # ユーザー登録入力画面を表示する
            self.remove_upload_file(users_entity_obj)
            self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])
            self.set_template_file_name('user_registration/input')

        # フォームの初期値を設定する為の初期化
        self.assign_all_form_data()
        # 複数選択項目の表示内容を取得して設定
        self.set_multiple_value_item()
        # 複数選択項目の選択状態を設定
        self.select_multiple_value_item()
    def remove_upload_file(self, users_entity_obj):
        if True == isinstance(users_entity_obj.file_name, str) and os.path.isfile(users_entity_obj.file_path):
            os.remove(users_entity_obj.file_path)
