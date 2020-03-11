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
    REQUIRED_MESSAGE = '{show_name}は必須項目です'
    NOT_EMPTY_MESSAGE = '{show_name}を入力してください'
    MIN_LENGTH_MESSAGE = '{show_name}は入力必要桁数に足りていません'
    MAX_LENGTH_MESSAGE = '{show_name}は入力可能桁数を超えています'
    MAIL_FORMAT_MESSAGE = '{show_name}の書式が不正です'
    MAIL_DOMAIN_MESSAGE = '{show_name}のドメインが存在しません'
    ALPHA_NUM_MESSAGE = '{show_name}は半角英数字で入力してください'
    JAPANESE_MESSAGE = '{show_name}は日本語で入力してください'
    JAPANESE_EXTEND_MESSAGE = '{show_name}は日本語で入力してください'
    HIRAGANA_MESSAGE = '{show_name}はひらがなで入力してください'
    NUMBER_MESSAGE = '{show_name}は数値を入力してください'
    INTEGER_MESSAGE = '{show_name}は整数を入力してください'
    RANGE_MESSAGE = '{show_name}は有効な値の範囲外です'
    DATE_MESSAGE = '{show_name}は不正な日付です'
    ZIP_CODE_FORMAT_MESSAGE = '{show_name}は不正な郵便番号です'
    TELEPHONE_FORMAT_MESSAGE = '{show_name}は不正な番号です'

    # 正規表現パターンのUnicodeコードポイント（ひらがな）
    PATTERN_HIRAGANA = '\u3041-\u3096'
    # 正規表現パターンのUnicodeコードポイント（カタカナ）
    PATTERN_KATAKANA = '\u30A1-\u30FA\u31F0-\u31FF\uFF66-\uFF6F\uFF71-\uFF9D'
    # 正規表現パターンのUnicodeコードポイント（濁点・半濁点）
    PATTERN_DAKUTEN = '\u3099\u309A\uFF9E\uFF9F'
    # 正規表現パターンのUnicodeコードポイント（長音）
    PATTERN_CHOON = '\u30FC'
    # 正規表現パターンのUnicodeコードポイント（漢字）(一部の文字は\p{Han}でも良いけど、明示的な方が良いかと)
    PATTERN_KANJI = '[\u2E80-\u2FDF\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u20000-\u2FFFF][\uE0100-\uE01EF\uFE00-\uFE02]'
    # 正規表現パターンのUnicodeコードポイント（全角英数字・半角英数字）
    PATTERN_ALL_WIDTH_ALPHABET_NUMBER = '\u0030-\u0039\u0041-\u005A\u0061-\u007A\uFF10-\uFF19\uFF41-\uFF5A'
    # 正規表現パターンのUnicodeコードポイント（以下の全角記号と全角スペース）
    # ‐ ― ‖ ‘ ’ “ ” ′ ″ ※ 　 、 。 〈 〉 《 》 「 」 『 』 【 】 〒 〔 〕 〖 〗 〜 〝 ！ ＂ ＃ ＄ ％ ＆ ＇ （ ） ＊ ＋ ， － ． ／ ： ； ＜ ＝ ＞ ？ ＠ ［ ＼ ］ ＾ ＿ ｀ ｛ ｜ ｝ ～ ￥
    PATTERN_FULL_WIDTH_SIGN = '\u2010\u2015\u2016\u2018\u2019\u201C-\u201D\u2032\u2033\u203B\u3000-\u3002\u3008-\u3012\u3014-\u3017\u301C-\u301D\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF5E\uFFE5'
    # 正規表現パターンのUnicodeコードポイント（全角数字）
    PATTERN_FULL_WIDTH_NUMBER = '\uFF10-\uFF19'
    # 正規表現パターンのUnicodeコードポイント（全角スペース）
    PATTERN_FULL_WIDTH_SPACE = '\u3000'

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
