import logging

class config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = False
    LOG_MAX_BYTES = 100000
    LOG_BACKUP_COUNT = 10
    LOG_LEVEL = logging.DEBUG
    PG_CHARACTER_SET = 'utf-8'
    USER_REGISTRATION_STATUS_REGISTERED = 1

    # ユーザー登録初期入力画面
    USER_REGISTRATION_FIRST_INPUT_TITLE = 'メールアドレス入力'

    # ユーザー登録初期入力完了画面
    USER_REGISTRATION_FIRST_COMPLETE_TITLE = 'メールアドレス入力完了'
    USER_REGISTRATION_FIRST_COMPLETE_REGISTERED_MESSAGE = '''メールアドレスの入力、ありがとうございます。
以下のURLより、登録を継続して下さい。

'''
    USER_REGISTRATION_FIRST_COMPLETE_ALREADY_REGISTERED_MESSAGE = '''メール入力画面でメールを入力されましたか？
誰かが、貴方のメールアドレスを入力したかもしれません。
ご注意下さい。'''
    USER_REGISTRATION_FIRST_COMPLETE_MAIL_TITLE = 'メール送信のお知らせ'

    # ユーザー登録入力画面
    USER_REGISTRATION_INPUT_TITLE = 'ユーザー登録'

class testing(config):
    ENV = 'testing'
    TESTING = True

class development(config):
    ENV = 'development'
    DEBUG = True

class production(config):
    ENV = 'production'
    SESSION_COOKIE_SECURE = True
    LOG_BACKUP_COUNT = 100
    LOG_LEVEL = logging.INFO
