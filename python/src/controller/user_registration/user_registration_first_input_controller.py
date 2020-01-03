from src.controller.user_registration import *

class user_registration_first_input_controller(controller):
    def execute(self):
        # メールアドレス入力画面を表示する
        self.add_response_data('title', setting.app.config['USER_REGISTRATION_FIRST_INPUT_TITLE'])
        self.add_response_data('mail_address', '')
        # CSRFトークンを作成する
        super().create_csrf_token()

        self.set_template_file_name('user_registration/index')
