from src.controller.user_registration import *

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
            title = 'メール送信のお知らせ'
            sender = setting.app.config['SENDER_MAIL_ADDRESS']
            recipients = user_obj.mail_address
            token = ''
            is_db_success = False
            if 0 < len(data):
                body = '''メール入力画面でメールを入力されましたか？
誰かが、貴方のメールアドレスを入力したかもしれません。
ご注意下さい。'''
                is_db_success = True
            else:
                token = secrets.token_hex(64)
                body = '''メールアドレスの入力、ありがとうございます。
以下のURLより、登録を継続して下さい。

'''
                body += setting.app.config['URI_SCHEME'] + '://' + setting.app.config['HOST_NAME'] + 'user_registration/input?m='
                body += recipients
                body += '&t=' + token
                # トークンを発行した場合には、DBに保存する
                user_obj.token = token
                #user_obj.begin()
                try:
                    user_obj.insert_raw(user_obj, ['mail_address', 'token', 'remarks'])
                    #user_obj.insert(user, [user_obj])
                    is_db_success = True
                except Exception as e:
                    user_obj.rollback()
            # メールを送信する
            is_mail_send = False
            if True == is_db_success:
                try:
                    msg = Message(title, sender=sender, recipients=[recipients])
                    msg.body = body
                    setting.mail.send(msg)
                    is_mail_send = True
                except Exception as e:
                    pass
            error_message = ''
            if True == is_db_success:
                if True == is_mail_send:
                    user_obj.commit()
                else:
                    user_obj.rollback()
                    error_message = 'メールの送信に失敗しました。'
            else:
                error_message = 'データベースへの登録に失敗しました。'
            if '' != error_message:
                raise Exception(error_message)
        else:
            template_file_name = 'user_registration/index'
            # CSRFトークンを作成する
            super().create_csrf_token()
            self.add_response_data('mail_address_error', validate_errors['error'][0]['message'])

        self.set_template_file_name(template_file_name)
