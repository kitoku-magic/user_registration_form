from src.controller.user_registration import *

class user_registration_first_complete_controller(user_registration_common_controller):
    """
    ユーザー登録の初期入力完了処理
    """
    def execute(self):
        # CSRFトークンをチェックする
        super().check_csrf_token()
        # メールアドレスのバリデーション
        pre_users_entity_obj = pre_users_entity()
        pre_users_entity_obj.set_request_to_entity(self.get_request().form)
        pre_users_entity_obj.set_validation_setting();
        validate_result = pre_users_entity_obj.validate();
        if True == validate_result:
            users_entity_obj = self.get_users_entity()
            users_repository_obj = users_repository(users_entity_obj)
            # 既に、ユーザー登録済みなら、メール文言を変える
            users_data = users_repository_obj.find(
                (users_entity.user_id,),
                'mail_address = :mail_address AND registration_status = :registration_status',
                collections.OrderedDict(
                    mail_address = pre_users_entity_obj.mail_address,
                    registration_status = setting.app.config['USER_REGISTRATION_STATUS_REGISTERED']
                )
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
                token = util.get_token_for_url(setting.app.config['SECRET_TOKEN_FOR_URL_BYTE_LENGTH'])
                pre_users_entity_obj.token = token
                body += setting.app.config['URI_SCHEME'] + '://' + setting.app.config['HOST_NAME'] + '/user_registration/input?mail_address='
                body += recipients
                body += '&token=' + token
                # まだ、事前情報が未登録なら、登録する
                pre_users_data = pre_users_repository_obj.find(
                    (pre_users_entity.pre_user_id,),
                    'mail_address = :mail_address',
                    collections.OrderedDict(
                        mail_address = pre_users_entity_obj.mail_address
                    ),
                    '',
                    True
                )
                update_column_name_list = pre_users_entity_obj.get_update_column_name_list()
                if pre_users_data is None:
                    try:
                        row_count = pre_users_repository_obj.insert(update_column_name_list)
                        if row_count > 0:
                            is_db_success = True
                            pre_user_id = pre_users_repository_obj.last_insert_id()
                    except Exception as exc:
                        setting.app.logger.exception('{}'.format(exc))
                        is_db_success = False
                else:
                    try:
                        row_count = pre_users_repository_obj.update(
                            update_column_name_list,
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
            title = setting.app.config['USER_REGISTRATION_FIRST_COMPLETE_MAIL_TITLE']
            is_mail_send = False
            if True == is_db_success:
                try:
                    # 入力されたメールアドレス宛にメールを送信する
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
                    error_message = setting.app.config['MAIL_SEND_ERROR']
            else:
                pre_users_repository_obj.rollback()
                error_message = setting.app.config['DB_REGISTRATION_ERROR']
            if '' != error_message:
                raise custom_exception(error_message, setting.app.config['SHOW_FIRST_COMPLETE_ERROR'])
            setting.app.logger.info('pre_user_id:' + str(pre_user_id) + 'にメールを送信しました。')
            template_file_name = 'user_registration/first_complete'
        else:
            # CSRFトークンを作成する
            super().create_csrf_token()
            self.add_response_data('mail_address_error', pre_users_entity_obj.mail_address_error)
            template_file_name = 'user_registration/index'

        self.set_template_common_data(setting.app.config['USER_REGISTRATION_FIRST_COMPLETE_TITLE'], template_file_name)
