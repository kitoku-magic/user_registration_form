from src.controller.user_registration import *

class user_registration_common_controller(controller):
    """
    ユーザー登録の、共通処理を定義するクラス
    """
    __abstract__ = True
    def __init__(self):
        super().__init__()
        request = self.get_request()
        # 使いやすさを考え、本処理を開始する前に、全てのフォームデータを設定しておく
        if 'GET' == request.environ['REQUEST_METHOD']:
            request_data = request.args
        elif 'POST' == request.environ['REQUEST_METHOD']:
            request_data = request.form
        self.__users_entity = users_entity()
        self.__users_entity.set_request_to_entity(request_data)
    @abstractmethod
    def execute(self):
        pass
    def get_users_entity(self):
        return self.__users_entity
    def assign_all_form_data(self):
        """
        全てのフォーム項目に値を設定する
        """
        properties = self.__users_entity.get_all_properties()
        for field, value in properties.items():
            if value is None:
                value = ''
            # DBから郵便番号を取得して表示する時は、ハイフンを付ける
            if 'zip_code' == field and '' != value and '-' not in value and self.__users_entity.zip_code_error is None:
                value = value[0:3] + '-' + value[3:]
            self.add_response_data(field, value)
    def set_value_item(self):
        """
        選択項目の表示内容を取得して設定
        """
        value_items = [
            # 性別
            {
                'repository': sexes_repository(sexes_entity()),
                'method': 'find_all',
                'select': ('sex_id','sex_name'),
                'where': '',
                'params': [],
                'order_by': 'sex_id ASC',
                'template_param_name': 'sexes',
            },
            # 都道府県
            {
                'repository': prefectures_repository(prefectures_entity()),
                'method': 'find_all',
                'select': ('prefecture_id','prefecture_name'),
                'where': '',
                'params': [],
                'order_by': 'prefecture_id ASC',
                'template_param_name': 'prefectures',
            },
            # 連絡方法
            {
                'repository': contact_methods_repository(contact_methods_entity()),
                'method': 'find_all',
                'select': ('contact_method_id','contact_method_name'),
                'where': '',
                'params': [],
                'order_by': 'contact_method_id ASC',
                'template_param_name': 'contact_methods',
            },
            # 知ったきっかけ
            {
                'repository': knew_triggers_repository(knew_triggers_entity()),
                'method': 'find_all',
                'select': ('knew_trigger_id','knew_trigger_name'),
                'where': '',
                'params': [],
                'order_by': 'knew_trigger_id ASC',
                'template_param_name': 'knew_triggers',
            },
        ]
        for value_item in value_items:
            result_data = getattr(value_item['repository'], value_item['method'])(
                value_item['select'],
                value_item['where'],
                value_item['params'],
                value_item['order_by']
            )
            response_data = []
            for row in result_data:
                response_dict = {'id': row[0], 'name': row[1]}
                response_data.append(response_dict)
            self.add_response_data(value_item['template_param_name'], response_data)
        # 以下は、特殊なケースの項目
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
        # 職業（その他を末尾に表示させる）
        jobs_repository_obj = jobs_repository(jobs_entity())
        jobs = jobs_repository_obj.find_all_order_by_job_other_last(
            ('job_id','job_name'),
            '',
            [],
            'job_id ASC'
        )
        self.add_response_data('jobs', jobs)
    def select_value_item(self):
        """
        選択項目の選択状態を設定
        """
        # 単一選択項目
        single_items = [
            {
                'name': 'birth_year',
                'default_value': '',
            },
            {
                'name': 'birth_month',
                'default_value': '',
            },
            {
                'name': 'birth_day',
                'default_value': '',
            },
            {
                'name': 'prefecture_id',
                'default_value': '',
            },
            {
                'name': 'sex_id',
                'default_value': 1,
            },
            {
                'name': 'job_id',
                'default_value': 2,
            },
            {
                'name': 'is_latest_news_hoped',
                'default_value': 1,
            },
            {
                'name': 'is_personal_information_provide_agreed',
                'default_value': '',
            },
        ]
        for single_item in single_items:
            form_value = getattr(self.__users_entity, single_item['name'], None)
            if form_value is None:
                value = single_item['default_value']
            else:
                value = form_value
            self.add_response_data(single_item['name'], value)
        # 複数選択項目
        multiple_items = [
            {
                'name': 'user_contact_methods_collection',
                'field': 'contact_method_id',
                'default_value': [],
            },
            {
                'name': 'user_knew_triggers_collection',
                'field': 'knew_trigger_id',
                'default_value': [],
            },
        ]
        for multiple_item in multiple_items:
            form_value = getattr(self.__users_entity, multiple_item['name'], None)
            if form_value is None:
                value = multiple_item['default_value']
            else:
                ids = []
                for entity in form_value:
                    ids.append(int(getattr(entity, multiple_item['field'], None)))
                value = ids
            self.add_response_data(multiple_item['name'], value)
    def remove_upload_file(self, users_entity_obj):
        """
        アップロードされたファイルを削除する
        """
        if True == isinstance(users_entity_obj.file_name, str) and os.path.isfile(users_entity_obj.file_path):
            os.remove(users_entity_obj.file_path)
