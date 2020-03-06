from src.controller.user_registration import *

class user_registration_confirm_controller(user_registration_common_controller):
    def execute(self):
        self.set_request_data(self.get_request().form)
        request_data = self.get_request_data()
        request_data_dict = request_data.to_dict()
        users_entity_obj = self.get_users_entity()
        properties = users_entity_obj.get_all_properties()
        for field, value in properties.items():
            if 'zip_code' == field:
                value = jaconv.z2h(request_data_dict[field], digit=True)
                setattr(users_entity_obj, field, value)
            else:
                if field in request_data_dict:
                    setattr(users_entity_obj, field, request_data_dict[field])
                else:
                    setattr(users_entity_obj, field, value)
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
        if 'street_address_search' == request_data.get('clicked_button'):
            is_next_page_forward = False
            if street_address_data is None:
                users_entity_obj.zip_code_error = '郵便番号に該当する住所が存在しません'
                users_entity_obj.prefecture_id = ''
                users_entity_obj.city_street_address = ''
            else:
                users_entity_obj.prefecture_id = street_address_data[0]
                users_entity_obj.city_street_address = street_address_data[1] + street_address_data[2]
        else:
            is_next_page_forward = True

        if True == is_next_page_forward:
            # ユーザー登録確認画面を表示する
            self.add_response_data('title', setting.app.config['USER_REGISTRATION_CONFIRM_TITLE'])
            self.set_template_file_name('user_registration/confirm')
        else:
            # ユーザー登録入力画面を表示する
            self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])
            self.set_template_file_name('user_registration/input')
        self.set_users_entity(users_entity_obj)

        # フォームの初期値を設定する為の初期化
        self.assign_all_form_data()
        # 複数選択項目の表示内容を取得して設定
        self.set_multiple_value_item()
        # 複数選択項目の選択状態を設定
        self.select_multiple_value_item()
