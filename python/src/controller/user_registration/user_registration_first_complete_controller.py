from src.controller.controller import controller
from src.model.user import user

class user_registration_first_complete_controller(controller):
    def execute(self):
        # 入力されたメールアドレス宛にメールを送信する
        self.add_response_data('title', 'メールアドレス入力完了')
        # CSRFトークンをチェックする
        super().check_csrf_token()
        post_data = self.get_request().form
        # メールアドレスのバリデーション
        user_obj = user()
        user_obj.set_request_to_model({'mail_address': ''}, post_data)
        validate_errors = user_obj.get_validate_errors()
        if True == validate_errors['result']:
            template_file_name = 'user_registration/first_complete'
            # メールアドレスがテーブルに存在していて、アカウントが登録済みなら、メール文言を変える
            data = user_obj.find(user.mail_address, 'mail_address = :mail_address AND registration_status = :registration_status', {'mail_address': user_obj.mail_address, 'registration_status': 1})
            # メールを送信する
            if 0 < len(data):
                print(data)
        else:
            template_file_name = 'user_registration/index'
            # CSRFトークンを作成する
            super().create_csrf_token()
            self.add_response_data('mail_address_error', validate_errors['error'][0]['message'])

        self.set_template_file_name(template_file_name)
