from src.controller.user_registration import *

class user_registration_first_complete_controller(controller):
    def execute(self):
        # 入力されたメールアドレス宛にメールを送信する
        self.add_response_data('title', 'メールアドレス入力完了')
        # CSRFトークンをチェックする
        super().check_csrf_token()
        post_data = self.get_request().form
        # メールアドレスのバリデーション
        pre_users_obj = pre_users()
        pre_users_obj.set_request_to_model({'mail_address': ''}, post_data)
        validate_errors = pre_users_obj.get_validate_errors()
        if True == validate_errors['result']:
            template_file_name = 'user_registration/first_complete'
            # 既に、ユーザー登録済みなら、メール文言を変える
            users_data = pre_users_obj.find(
                    ('user_id',),
                    'users',
                    'mail_address = %s AND registration_status = %s',
                    (pre_users_obj.mail_address, 1)
            )
            sender = setting.app.config['SENDER_MAIL_ADDRESS']
            recipients = pre_users_obj.mail_address
            token = ''
            is_db_success = False
            if users_data is None:
                body = '''メールアドレスの入力、ありがとうございます。
以下のURLより、登録を継続して下さい。

'''
                token = secrets.token_hex(64)
                pre_users_obj.token = token
                body += setting.app.config['URI_SCHEME'] + '://' + setting.app.config['HOST_NAME'] + '/user_registration/input?m='
                body += recipients
                body += '&t=' + token
                # まだ、事前情報が未登録なら、登録する
                pre_users_data = pre_users_obj.find(
                    ('pre_user_id',),
                    'pre_users',
                    'mail_address = %s',
                    (pre_users_obj.mail_address,)
                )
                if pre_users_data is None:
                    #pre_users_obj.begin()
                    try:
                        row_count = pre_users_obj.insert(['mail_address', 'token'])
                        if row_count > 0:
                            is_db_success = True
                    except Exception as e:
                        print(e)
                        is_db_success = False
                else:
                    #pre_users_obj.begin()
                    try:
                        row_count = pre_users_obj.update(
                            ['token'],
                            'pre_user_id = %s',
                            (pre_users_data[0],)
                        )
                        if row_count > 0:
                            is_db_success = True
                    except Exception as e:
                        print(e)
                        is_db_success = False
            else:
                body = '''メール入力画面でメールを入力されましたか？
誰かが、貴方のメールアドレスを入力したかもしれません。
ご注意下さい。'''
                is_db_success = True
            # メールを送信する
            title = 'メール送信のお知らせ'
            is_mail_send = False
            if True == is_db_success:
                try:
                    msg = Message(title, sender=sender, recipients=[recipients])
                    msg.body = body
                    setting.mail.send(msg)
                    is_mail_send = True
                except Exception as e:
                    print(e)
                    is_mail_send = False
            error_message = ''
            if True == is_db_success:
                if True == is_mail_send:
                    pre_users_obj.commit()
                else:
                    pre_users_obj.rollback()
                    error_message = 'メールの送信に失敗しました。'
            else:
                pre_users_obj.rollback()
                error_message = 'データベースへの登録に失敗しました。'
            if '' != error_message:
                raise Exception(error_message)
        else:
            template_file_name = 'user_registration/index'
            # CSRFトークンを作成する
            super().create_csrf_token()
            self.add_response_data('mail_address_error', validate_errors['error'][0]['message'])

        self.set_template_file_name(template_file_name)
