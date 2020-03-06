from src.controller.user_registration import *

class user_registration_common_controller(controller):
    def __init__(self):
        super().__init__()
        request = self.get_request()
        if 'GET' == request.environ['REQUEST_METHOD']:
            request_data = request.args
        elif 'POST' == request.environ['REQUEST_METHOD']:
            request_data = request.form
        self.__users_entity = users_entity()
        self.__users_entity.set_request_to_model(request_data)
    def set_users_entity(self, users_entity):
        self.__users_entity = users_entity
    def get_users_entity(self):
        return self.__users_entity
    # フォームの初期値を設定する為の初期化
    def assign_all_form_data(self):
        properties = self.__users_entity.get_all_properties()
        for field, value in properties.items():
            if value is None:
                value = ''
            self.add_response_data(field, value)
    # 複数選択項目の表示内容を取得して設定
    def set_multiple_value_item(self):
        # 性別
        sexes_repository_obj = sexes_repository(sexes_entity())
        sexes_all_data = sexes_repository_obj.find_all(
            ('sex_id','sex_name'),
            '',
            [],
            'sex_id ASC'
        )
        sexes = []
        for row in sexes_all_data:
            sexes_dict = {'id': row[0], 'name': row[1]}
            sexes.append(sexes_dict)
        self.add_response_data('sexes', sexes)
        # 誕生日
        birth_days_repository_obj = birth_days_repository(birth_days_entity())
        birth_days_all_data = birth_days_repository_obj.find_all(
            ('birth_day_id','birth_day'),
            '',
            [],
            'birth_day_id ASC'
        )
        birth_years = []
        birth_months = []
        birth_days = []
        for row in birth_days_all_data:
            if row[1].year not in birth_years:
                birth_years.append(row[1].year)
            if row[1].month not in birth_months:
                birth_months.append(row[1].month)
            if row[1].day not in birth_days:
                birth_days.append(row[1].day)
        self.add_response_data('birth_years', birth_years)
        self.add_response_data('birth_months', birth_months)
        self.add_response_data('birth_days', birth_days)
        # 都道府県
        prefectures_repository_obj = prefectures_repository(prefectures_entity())
        prefectures_all_data = prefectures_repository_obj.find_all(
            ('prefecture_id','prefecture_name'),
            '',
            [],
            'prefecture_id ASC'
        )
        prefectures = []
        for row in prefectures_all_data:
            prefectures_dict = {'id': row[0], 'name': row[1]}
            prefectures.append(prefectures_dict)
        self.add_response_data('prefectures', prefectures)
        # 職業
        jobs_repository_obj = jobs_repository(jobs_entity())
        jobs_all_data = jobs_repository_obj.find_all(
            ('job_id','job_name'),
            '',
            [],
            'job_id ASC'
        )
        jobs = []
        for row in jobs_all_data:
            jobs_dict = {'id': row[0], 'name': row[1]}
            jobs.append(jobs_dict)
        self.add_response_data('jobs', jobs)
        # 連絡方法
        contact_methods_repository_obj = contact_methods_repository(contact_methods_entity())
        contact_methods_all_data = contact_methods_repository_obj.find_all(
            ('contact_method_id','contact_method_name'),
            '',
            [],
            'contact_method_id ASC'
        )
        contact_methods = []
        for row in contact_methods_all_data:
            contact_methods_dict = {'id': row[0], 'name': row[1]}
            contact_methods.append(contact_methods_dict)
        self.add_response_data('contact_methods', contact_methods)
        # 知ったきっかけ
        knew_triggers_repository_obj = knew_triggers_repository(knew_triggers_entity())
        knew_triggers_all_data = knew_triggers_repository_obj.find_all(
            ('knew_trigger_id','knew_trigger_name'),
            '',
            [],
            'knew_trigger_id ASC'
        )
        knew_triggers = []
        for row in knew_triggers_all_data:
            knew_triggers_dict = {'id': row[0], 'name': row[1]}
            knew_triggers.append(knew_triggers_dict)
        self.add_response_data('knew_triggers', knew_triggers)
    # 複数選択項目の選択状態を設定
    def select_multiple_value_item(self):
        self.create_select_box('birth_year', '')
        self.create_select_box('birth_month', '')
        self.create_select_box('birth_day', '')
        self.create_select_box('prefecture_id', '')

        self.create_radio_box('sex_id', 1)
        self.create_radio_box('job_id', 1)
        self.create_radio_box('is_latest_news_hoped', 1)

        self.create_check_box('is_personal_information_provide_agreed', '')

        self.create_multiple_select_box('contact_method', [])

        self.create_multiple_check_box('knew_trigger', [])
    def create_select_box(self, key, select_value):
        if 'previous_page' == self.__users_entity.clicked_button:
            print('previous_page')
            print(self.__users_entity)
        else:
            form_value = getattr(self.__users_entity, key, None)
            if form_value is None:
                value = select_value
            else:
                value = form_value
        self.add_response_data(key, value)
    def create_radio_box(self, key, select_value):
        form_value = getattr(self.__users_entity, key, None)
        if form_value is None:
            value = select_value
        else:
            value = form_value
        self.add_response_data(key, value)
    def create_check_box(self, key, select_value):
        form_value = getattr(self.__users_entity, key, None)
        if form_value is None:
            value = select_value
        else:
            value = form_value
        self.add_response_data(key, value)
    def create_multiple_select_box(self, key, select_value):
        if 'previous_page' == self.__users_entity.clicked_button:
            print('previous_page')
            print(self.__users_entity)
        else:
            form_value = getattr(self.__users_entity, key, None)
            if form_value is None:
                value = select_value
            else:
                value = form_value
        self.add_response_data(key, value)
    def create_multiple_check_box(self, key, select_value):
        if 'previous_page' == self.__users_entity.clicked_button:
            print('previous_page')
            print(self.__users_entity)
        else:
            form_value = getattr(self.__users_entity, key, None)
            if form_value is None:
                value = select_value
            else:
                value = form_value
        self.add_response_data(key, value)
