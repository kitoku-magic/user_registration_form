# テンプレートファイルから呼び出すfilter関数群

from markupsafe import Markup

def nl2br(value):
    """
    改行コードを、HTMLの改行に変換する
    """
    value = value.__str__().replace('\n', '<br />')
    return Markup(value)
