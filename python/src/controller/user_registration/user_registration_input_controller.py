from src.controller.user_registration import *

class user_registration_input_controller(controller):
    __all_tmp_user = None
    def execute(self):
        # ユーザー登録入力画面を表示する
        self.add_response_data('title', setting.app.config['USER_REGISTRATION_INPUT_TITLE'])

        get_data = self.get_request().args
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
