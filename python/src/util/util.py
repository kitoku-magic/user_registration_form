import dns.resolver
import re
import unicodedata

from src.util import *

class util:
    def check_mail_address(value, max_length):
        ret = 0
        if value == '':
            ret = 1
        elif max_length < len(value.encode(setting.app.config['PG_CHARACTER_SET'])):
            ret = 2
        elif '@' not in value:
            ret = 3
        else:
            tmp = value.split('@')
            mail_domain = tmp[-1]
            try:
                records  = dns.resolver.query(mail_domain, 'MX')
                mx_record = records[0].exchange
                mxRecord = str(mx_record)
            except Exception as exc:
                ret = 4
        return ret
    def replace_hyphen(value, replace):
        return re.sub('\u002D|\uFE63|\uFF0D|\u2010|\u2011|\u2043|\u02D7|\u2212|\u2012|\u2013|\u2014|\u2015|\uFE58|\u23AF|\u23E4|\u268A|\u2500|\u1173|\u2F00|\u30FC|\u3161|\u31D0|\u4E00|\uFF70|\uFFDA', replace, value)
    def mb_trim(value, character_mask):
        return value.strip(character_mask)
    def join_diacritic(value, mode='NFC'):
        """
        基底文字と濁点・半濁点を結合する
        @see https://qiita.com/syamamura/items/13c0825282415e2e360d
        """
        bytes_value = value.encode()

        # 濁点Unicode結合文字置換
        bytes_value = re.sub(b"\xe3\x82\x9b", b'\xe3\x82\x99', bytes_value)
        bytes_value = re.sub(b"\xef\xbe\x9e", b'\xe3\x82\x99', bytes_value)

        # 半濁点Unicode結合文字置換
        bytes_value = re.sub(b"\xe3\x82\x9c", b'\xe3\x82\x9a', bytes_value)
        bytes_value = re.sub(b"\xef\xbe\x9f", b'\xe3\x82\x9a', bytes_value)

        value = bytes_value.decode()

        return unicodedata.normalize(mode, value)
    def is_empty(value):
        """
        空かどうかのチェック
        """
        return value is None or '' == value
