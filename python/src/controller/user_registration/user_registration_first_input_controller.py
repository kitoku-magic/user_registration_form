from src.controller.controller import controller

class user_registration_first_input_controller(controller):
    def execute(self):
        # メールアドレス入力画面を表示する
        self.add_response_data('title', 'メールアドレス入力')
        self.add_response_data('mail_address', '')
        # CSRFトークンを作成する
        super().create_csrf_token()

        self.set_template_file_name('user_registration/index')
