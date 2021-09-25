from src.application import app
from src.controller.user_registration.user_registration_common_controller import user_registration_common_controller

class user_registration_first_input_controller(user_registration_common_controller):
    """
    ユーザー登録の、初期入力処理
    """
    def execute(self):
        self.add_response_data('mail_address', '')
        # CSRFトークンを作成する
        super().create_csrf_token()

        # メールアドレス入力画面を表示する
        self.set_template_common_data(app.config['USER_REGISTRATION_FIRST_INPUT_TITLE'], 'user_registration/index')
