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

    # バリデーションエラーメッセージ
    REQUIRED_MESSAGE = '{show_name}は必須項目です';
    NOT_EMPTY_MESSAGE = '{show_name}を入力してください';
    MIN_LENGTH_MESSAGE = '{show_name}は入力必要桁数に足りていません';
    MAX_LENGTH_MESSAGE = '{show_name}は入力可能桁数を超えています';
    MAIL_FORMAT_MESSAGE = '{show_name}の書式が不正です';
    ALPHA_NUM_MESSAGE = '{show_name}は半角英数字で入力してください';
    JAPANESE_MESSAGE = '{show_name}は日本語で入力してください';
    JAPANESE_EXTEND_MESSAGE = '{show_name}は日本語で入力してください';
    HIRAGANA_MESSAGE = '{show_name}はひらがなで入力してください';
    NUMBER_MESSAGE = '{show_name}は数値を入力してください';
    INTEGER_MESSAGE = '{show_name}は整数を入力してください';
    RANGE_MESSAGE = '{show_name}は有効な値の範囲外です';
    DATE_MESSAGE = '{show_name}は不正な日付です';
    ZIP_CODE_FORMAT_MESSAGE = '{show_name}は不正な郵便番号です';
    TELEPHONE_FORMAT_MESSAGE = '{show_name}は不正な番号です';

    # ユーザー登録初期入力画面
    USER_REGISTRATION_FIRST_INPUT_TITLE = 'メールアドレス入力'

    # ユーザー登録初期入力完了画面
    USER_REGISTRATION_FIRST_COMPLETE_TITLE = 'メールアドレス入力完了'
    USER_REGISTRATION_FIRST_COMPLETE_REGISTERED_MESSAGE = '''メールアドレスの入力、ありがとうございます。
以下のURLより、登録を継続して下さい。
また、URLの有効期間は１時間となっておりますので、ご注意下さい。

'''
    USER_REGISTRATION_FIRST_COMPLETE_ALREADY_REGISTERED_MESSAGE = '''メール入力画面でメールを入力されましたか？
誰かが、貴方のメールアドレスを入力したかもしれません。
ご注意下さい。'''
    USER_REGISTRATION_FIRST_COMPLETE_MAIL_TITLE = 'メール送信のお知らせ'

    # ユーザー登録入力画面
    USER_REGISTRATION_INPUT_TITLE = 'ユーザー登録'

    # ユーザー登録確認画面
    USER_REGISTRATION_CONFIRM_TITLE = 'ユーザー登録確認'
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
