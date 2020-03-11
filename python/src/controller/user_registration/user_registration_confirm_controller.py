from src.controller.user_registration import *

class user_registration_confirm_controller(user_registration_common_controller):
    def execute(self):
        request = self.get_request()
        request_form = request.form
        request_files = request.files
        users_entity_obj = self.get_users_entity()
        users_entity_obj.user_contact_methods_collection = request_form.getlist('contact_method')
        users_entity_obj.user_knew_triggers_collection = request_form.getlist('knew_trigger')
        users_entity_obj.upload_file_list = request_files.getlist('file_name')
        users_entity_obj.trim_all_data()
        properties = users_entity_obj.get_all_properties()
        for field, value in properties.items():
            if 'last_name' == field or 'first_name' == field:
                value = jaconv.h2z(value)
                value = util.join_diacritic(value)
            elif 'last_name_hiragana' == field or 'first_name_hiragana' == field:
                value = jaconv.kata2hira(jaconv.h2z(value))
                value = util.join_diacritic(value)
            elif 'zip_code' == field or 'telephone_number' == field:
                value = jaconv.z2h(value, digit=True)
                value = util.replace_hyphen(value, '-')
            elif 'city_street_address' == field or 'building_room_address' == field or 'job_other' == field:
                value = jaconv.h2z(value, kana=True, digit=True, ascii=True)
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
            ('prefecture_id', 'city_district_county', 'town_village_address'),
            'zip_code = %s',
            (zip_codes[0] + zip_codes[1],)
        )
        if 'street_address_search' == users_entity_obj.clicked_button:
            is_next_page_forward = False
            if street_address_data is None:
                users_entity_obj.zip_code_error = '郵便番号に該当する住所が存在しません'
                users_entity_obj.prefecture_id = ''
                users_entity_obj.city_street_address = ''
            else:
                users_entity_obj.prefecture_id = street_address_data[0]
                users_entity_obj.city_street_address = street_address_data[1] + street_address_data[2]
        elif 'next_page' == users_entity_obj.clicked_button:
            is_next_page_forward = True
            users_entity_obj.set_validation_setting();
            is_next_page_forward = users_entity_obj.validate();
            # 郵便番号の存在結果
            if users_entity_obj.zip_code_error is None and street_address_data is None:
                is_next_page_forward = false;
                users_entity_obj.zip_code_error = '郵便番号に該当する住所が存在しません'
                users_entity_obj.prefecture_id = ''
                users_entity_obj.city_street_address = ''
        else:
            raise custom_exception('不正なリクエストです')

        if True == is_next_page_forward:
            # ユーザー登録確認画面を表示する
            self.add_response_data('title', setting.app.config['USER_REGISTRATION_CONFIRM_TITLE'])
            self.set_template_file_name('user_registration/confirm')
        else:
            # ユーザー登録入力画面を表示する
            self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])
            self.set_template_file_name('user_registration/input')

        # フォームの初期値を設定する為の初期化
        self.assign_all_form_data()
        # 複数選択項目の表示内容を取得して設定
        self.set_multiple_value_item()
        # 複数選択項目の選択状態を設定
        self.select_multiple_value_item()
