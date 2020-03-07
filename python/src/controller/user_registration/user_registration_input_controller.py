from src.controller.user_registration import *

class user_registration_input_controller(user_registration_common_controller):
    __all_tmp_user = None
    def execute(self):
        # ユーザー登録入力画面を表示する
        self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])

        users_entity_obj = self.get_users_entity()
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
            print('previous_page')
            print(users_entity_obj)
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
        # フォームの初期値を設定する為の初期化
        self.assign_all_form_data()
        # 複数選択項目の表示内容を取得して設定
        self.set_multiple_value_item()
        # 複数選択項目の選択状態を設定
        self.select_multiple_value_item()

        self.set_template_file_name('user_registration/input')
    def set_all_tmp_user(self, all_tmp_user):
        __all_tmp_user = all_tmp_user
    def get_all_tmp_user(self):
        return self.__all_tmp_user
