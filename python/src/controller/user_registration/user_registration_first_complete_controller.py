from controller.controller import controller

class user_registration_first_complete_controller(controller):
    def execute(self):
        # 入力されたメールアドレス宛にメールを送信する
        self.set_response_data('title', 'メールアドレス入力完了')
        # CSRFトークンをチェックする
        super().check_csrf_token()
        post_data = self.get_post_data()
        # メールアドレスのバリデーション（桁数と書式チェックのみ）
        # メアドがテーブルに存在していて、アカウントが登録済みなら、メール文言を変える
        # メールを送信する

        self.set_template_file_name('user_registration/first_complete')
