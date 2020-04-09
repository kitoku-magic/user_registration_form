from src.controller.user_registration import *

class user_registration_confirm_controller(user_registration_common_controller):
    """
    ユーザー登録の、確認処理
    """
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
            # jaconvの関数の引数はstring型にする必要がある
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
            # 住所検索ボタン押下時は、画面遷移をしない
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
            # バリデーション時に、ファイルアップロードだけは、アップロード処理も行われる
            is_next_page_forward = users_entity_obj.validate();
            # 郵便番号の存在結果
            if users_entity_obj.zip_code_error is None:
                if street_address_data is None:
                    is_next_page_forward = False;
                    users_entity_obj.zip_code_error = setting.app.config['ZIP_CODE_ERROR']
                    users_entity_obj.prefecture_id = ''
                    users_entity_obj.city_street_address = ''
                elif users_entity_obj.prefecture_id != street_address_data[1]:
                    # 郵便番号が属する都道府県になっていない時のエラー
                    is_next_page_forward = False;
                    users_entity_obj.prefecture_id_error = setting.app.config['ZIP_CODE_CONSISTENCY_ERROR']
        else:
            raise custom_exception(setting.app.config['INVALID_REQUEST_ERROR'])

        if True == is_next_page_forward:
            # 誕生日存在チェック
            birth_days_repository_obj = birth_days_repository(birth_days_entity())
            birth_days_data = birth_days_repository_obj.find(
                ('birth_day_id',),
                'birth_day = %s',
                (users_entity_obj.birth_day_full,)
            )
            if birth_days_data is None:
                is_next_page_forward = False
                users_entity_obj.birth_day_full_error = setting.app.config['BIRTH_DAY_NOT_REGISTRATION_ERROR']
            else:
                users_entity_obj.birth_day_id = birth_days_data[0]

        if True == is_next_page_forward:
            users_repository_obj = users_repository(users_entity_obj)
            users_repository_obj.begin()
            try:
                # ユーザー登録済みチェック
                is_user_exist = True
                users_data = users_repository_obj.find(
                    ('user_id','registration_status'),
                    'mail_address = %s',
                    (users_entity_obj.mail_address,),
                    '',
                    True
                )
                if users_data is None:
                    is_user_exist = False
                else:
                    if setting.app.config['USER_REGISTRATION_STATUS_REGISTERED'] != users_data[1]:
                        is_user_exist = False
                        users_entity_obj.user_id = users_data[0]
                if True == is_user_exist:
                    raise custom_exception(
                        setting.app.config['MAIL_ADDRESS_REGISTRATIONED_ERROR'],
                        setting.app.config['SHOW_MAIL_ADDRESS_REGISTRATIONED_ERROR']
                    )
                if users_entity_obj.file_path is None:
                    users_entity_obj.file_name = ''
                    users_entity_obj.file_path = ''
                if setting.app.config['JOB_ID_OTHER'] != users_entity_obj.job_id:
                    users_entity_obj.job_other = ''
                users_entity_obj.input_token = users_entity_obj.token
                users_entity_obj.registration_status = setting.app.config['USER_REGISTRATION_STATUS_REGISTERING']
                users_entity_obj.token = util.get_token_for_url(setting.app.config['SECRET_TOKEN_FOR_URL_BYTE_LENGTH'])
                users_entity_obj.zip_code = zip_codes[0] + zip_codes[1]
                update_column_name_list = users_entity_obj.get_update_column_name_list()
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
                    raise custom_exception(setting.app.config['USER_TEMPORARY_SAVE_ERROR'])
                users_repository_obj.commit()
            except Exception as exc:
                users_repository_obj.rollback()
                self.remove_upload_file(users_entity_obj)
                if True == isinstance(exc, custom_exception):
                    if 1 < len(exc.args):
                        show_error_message = exc.args[1]
                    else:
                        show_error_message = setting.app.config['SHOW_SYSTEM_ERROR']
                else:
                    show_error_message = setting.app.config['SHOW_SYSTEM_ERROR']
                raise custom_exception(
                    str(exc),
                    show_error_message
                )
            # ユーザー登録確認画面を表示する
            self.set_template_common_data(setting.app.config['USER_REGISTRATION_CONFIRM_TITLE'], 'user_registration/confirm')
        else:
            # 画面遷移しない時は、アップロードされたファイルを削除
            self.remove_upload_file(users_entity_obj)
            # ユーザー登録入力画面を表示する
            self.set_template_common_data(setting.app.config['USER_REGISTRATION_INPUT_TITLE'], 'user_registration/input')

        # 全てのフォーム項目に値を設定する
        self.assign_all_form_data()
        # 選択項目の表示内容を取得して設定
        self.set_value_item()
        # 選択項目の選択状態を設定
        self.select_value_item()
