from src.controller.user_registration import *

class user_registration_input_controller(controller):
    __all_tmp_user = None
    def execute(self):
        # ユーザー登録入力画面を表示する
        self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])

        get_data = self.get_request().args
        pre_users_repository_obj = pre_users_repository(pre_users_entity())
        # メールアドレスとトークンが一致して、現在時間が最終更新時間から１時間経っていなければOK
        pre_users_data = pre_users_repository_obj.find(
            ('pre_user_id',),
            'mail_address = %s AND token = %s AND updated_at >= %s',
            (get_data.get('mail_address'), get_data.get('token'), (math.floor(time.time()) - 3600))
        )
        if pre_users_data is None:
            raise Exception(
                'URLの有効期限が切れています。',
                'URLの有効期限が切れています。\n再度、メールアドレス入力画面からお手続き下さい。'
            )
        if 'previous_page' == get_data.get('clicked_button'):
            print('previous_page')
            print(get_data)
        # フォームの初期値を設定する為の初期化
        users_entity_obj = users_entity()
        get_data_dict = get_data.to_dict()
        properties = users_entity_obj.get_all_properties()
        for field, value in properties.items():
            if field in get_data_dict.keys():
                value = get_data.get(field)
            self.add_response_data(field, value)
        # 複数選択項目の表示内容を取得して設定
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
        prefectureses = []
        for row in prefectures_all_data:
            prefectureses_dict = {'id': row[0], 'name': row[1]}
            prefectureses.append(prefectureses_dict)
        self.add_response_data('prefectureses', prefectureses)
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

#        $template_convert = $this->get_template_convert();
#
#    // 複数選択可能な項目のデータを取得
#    $storage_handlers = $this->get_storage_handlers();
#    $multiple_select_category_repository = new multiple_select_category_repository_impl(
#            $storage_handlers,
#            new multiple_select_repository_impl($storage_handlers)
#            );
#    $this->multiple_select_category_data = $multiple_select_category_repository->get_all_multiple_select();
#
#    $category_mappings = array(
#            // 連絡方法
#            1 => array(
#                'name' => 'contact_method',
#                'names' => 'contact_methods',
#                ),
#            // 知ったきっかけ
#            2 => array(
#                'name' => 'knew_trigger',
#                'names' => 'knew_triggeres',
#                ),
#            );
#    foreach ($this->multiple_select_category_data as $multiple_select_category)
#    {
#            $template_convert->assign_single_array($category_mappings[$multiple_select_category->get_multiple_select_category_id()]['name'], $multiple_select_category->get_name());
#            $template_convert->assign_bool_array($category_mappings[$multiple_select_category->get_multiple_select_category_id()]['names'], $multiple_select_category->get_multiple_select_entities());
#            }
#
#    // 単一選択な項目のデータを取得
#    $single_select_category_repository = new single_select_category_repository_impl(
#            $storage_handlers,
#            new single_select_repository_impl($storage_handlers)
#            );
#    $single_select_category_data = $single_select_category_repository->get_all_single_select();
#
#    $category_mappings = array(
#            // 性別
#            1 => array(
#                'name' => 'sex',
#                'names' => 'sexes',
#                ),
#            // 誕生日（年）
#            2 => array(
#                'name' => 'birth_year',
#                'names' => 'birth_years',
#                ),
#            // 誕生日（月）
#            3 => array(
#                'name' => 'birth_month',
#                'names' => 'birth_months',
#                ),
#            // 誕生日（日）
#            4 => array(
#                'name' => 'birth_day',
#                'names' => 'birth_days',
#                ),
#            // 都道府県
#            5 => array(
#                'name' => 'prefectures',
#                'names' => 'prefectureses',
#                ),
#            // 職業
#            6 => array(
#                'name' => 'job',
#                'names' => 'jobs',
#                ),
#            );
#    foreach ($single_select_category_data as $single_select_category)
#    {
#            $template_convert->assign_single_array($category_mappings[$single_select_category->get_single_select_category_id()]['name'], $single_select_category->get_name());
#            $template_convert->assign_bool_array($category_mappings[$single_select_category->get_single_select_category_id()]['names'], $single_select_category->get_single_select_entities());
#            }






#        $form = $this->get_form()
#        if ('previous_page' === $form->get_clicked_button())
#        {
#            $storage_handlers = $this->get_storage_handlers()
#            $tmp_user_repository = new tmp_user_repository_impl(
#                $storage_handlers,
#                new tmp_user_multiple_select_repository_impl($storage_handlers)
#            )
#            $this->all_tmp_user = $tmp_user_repository->get_all_tmp_user($form->get_tmp_user_id(), $form->get_token())
#            foreach ($this->all_tmp_user as $tmp_user)
#            {
#                $entity_table_columns = $tmp_user->get_table_columns()
#                foreach ($entity_table_columns as $table_column => $value)
#                {
#                    $getter = 'get_' . $table_column
#                    if ('password' === $table_column)
#                    {
#                        // パスワードは表示させない
#                        $entity_value = ''
#                    }
#                    else
#                    {
#                        $entity_value = $tmp_user->$getter()
#                    }
#                    $form->execute_accessor_method('set', $table_column, $entity_value)
#                }
#            }
#        }
#
#        // フォームの初期値を設定する為の初期化
#        $this->assign_all_form_data()
#
#        // 複数選択項目の表示内容を取得して設定
#        $this->set_multiple_value_item()
#
#        // 複数選択項目の初期選択状態を設定
#        $this->select_multiple_value_item()

        self.set_template_file_name('user_registration/input')
    def set_all_tmp_user(self, all_tmp_user):
        __all_tmp_user = all_tmp_user
    def get_all_tmp_user(self):
        return self.__all_tmp_user
