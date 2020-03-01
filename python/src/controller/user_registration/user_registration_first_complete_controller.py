from src.controller.user_registration import *

class user_registration_first_complete_controller(controller):
    def execute(self):
        # 入力されたメールアドレス宛にメールを送信する
        self.add_response_data('title', setting.app.config['USER_REGISTRATION_FIRST_COMPLETE_TITLE'])
        # CSRFトークンをチェックする
        super().check_csrf_token()
        post_data = self.get_request().form
        # メールアドレスのバリデーション
        pre_users_entity_obj = pre_users_entity()
        pre_users_entity_obj.set_request_to_model({'mail_address': ''}, post_data)
        validate_errors = pre_users_entity_obj.get_validate_errors()
        if True == validate_errors['result']:
            template_file_name = 'user_registration/first_complete'
            users_repository_obj = users_repository(users_entity())
            # 既に、ユーザー登録済みなら、メール文言を変える
            users_data = users_repository_obj.find(
                    ('user_id',),
                    'mail_address = %s AND registration_status = %s',
                    (pre_users_entity_obj.mail_address, setting.app.config['USER_REGISTRATION_STATUS_REGISTERED'])
            )
            sender = setting.app.config['SENDER_MAIL_ADDRESS']
            recipients = pre_users_entity_obj.mail_address
            pre_user_id = 0
            token = ''
            is_db_success = False
            pre_users_repository_obj = pre_users_repository(pre_users_entity_obj)
            pre_users_repository_obj.begin()
            if users_data is None:
                body = setting.app.config['USER_REGISTRATION_FIRST_COMPLETE_REGISTERED_MESSAGE']
                token = secrets.token_hex(64)
                pre_users_entity_obj.token = token
                body += setting.app.config['URI_SCHEME'] + '://' + setting.app.config['HOST_NAME'] + '/user_registration/input?mail_address='
                body += recipients
                body += '&token=' + token
                # まだ、事前情報が未登録なら、登録する
                pre_users_data = pre_users_repository_obj.find(
                    ('pre_user_id',),
                    'mail_address = %s',
                    (pre_users_entity_obj.mail_address,),
                    '',
                    True
                )
                if pre_users_data is None:
                    try:
                        row_count = pre_users_repository_obj.insert(['mail_address', 'token'])
                        if row_count > 0:
                            is_db_success = True
                            pre_user_id = pre_users_repository_obj.last_insert_id()
                    except Exception as exc:
                        setting.app.logger.exception('{}'.format(exc))
                        is_db_success = False
                else:
                    try:
                        row_count = pre_users_repository_obj.update(
                            ['token'],
                            'pre_user_id = %s',
                            (pre_users_data[0],)
                        )
                        if row_count > 0:
                            is_db_success = True
                            pre_user_id = pre_users_data[0]
                    except Exception as exc:
                        setting.app.logger.exception('{}'.format(exc))
                        is_db_success = False
            else:
                body = setting.app.config['USER_REGISTRATION_FIRST_COMPLETE_ALREADY_REGISTERED_MESSAGE']
                is_db_success = True
                pre_user_id = users_data[0]
            # メールを送信する
            title = setting.app.config['USER_REGISTRATION_FIRST_COMPLETE_MAIL_TITLE']
            is_mail_send = False
            if True == is_db_success:
                try:
                    msg = Message(title, sender=sender, recipients=[recipients])
                    msg.body = body
                    setting.mail.send(msg)
                    is_mail_send = True
                except Exception as exc:
                    setting.app.logger.exception('{}'.format(exc))
                    is_mail_send = False
            error_message = ''
            if True == is_db_success:
                if True == is_mail_send:
                    pre_users_repository_obj.commit()
                else:
                    pre_users_repository_obj.rollback()
                    error_message = 'メールの送信に失敗しました。'
            else:
                pre_users_repository_obj.rollback()
                error_message = 'データベースへの登録に失敗しました。'
            if '' != error_message:
                raise Exception(error_message, '登録に失敗しました。\n再度、お手続き下さい。')
            setting.app.logger.info('pre_user_id:' + str(pre_user_id) + 'にメールを送信しました。')
        else:
            template_file_name = 'user_registration/index'
            # CSRFトークンを作成する
            super().create_csrf_token()
            self.add_response_data('mail_address_error', validate_errors['error'][0]['message'])

        self.set_template_file_name(template_file_name)
