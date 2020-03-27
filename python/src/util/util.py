import dns.resolver
import secrets
import os
import re
import unicodedata
import uuid
from datetime import datetime

from src.util import *

class util:
    def check_mail_format(value):
        return '@' in value
    def check_mail_domain(value):
        ret = True
        tmp = value.split('@')
        mail_domain = tmp[-1]
        try:
            records  = dns.resolver.query(mail_domain, 'MX')
            mx_record = records[0].exchange
            mxRecord = str(mx_record)
        except Exception as exc:
            ret = False
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
    def check_min_length(value, length):
        """
        最小桁数のチェック
        """
        return len(value.encode('utf-8')) >= length
    def check_max_length(value, length):
        """
        最大桁数のチェック
        """
        return len(value.encode('utf-8')) <= length
    def check_date(date, date_format = '%Y-%m-%d %H:%M:%S'):
        """
        日付が妥当かどうかのチェック
        """
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False
    def check_zip_code(value, is_include_hyphen = False):
        """
        郵便番号が妥当かどうかのチェック
        """
        pattern = '\A[0-9]{3}'
        if True == is_include_hyphen:
            pattern += '-'
        pattern += '[0-9]{4}\Z'
        return re.match(pattern, value) is not None
    def check_telephone(value, is_include_hyphen = False):
        """
        電話番号が妥当かどうかのチェック
        """
        pattern = '\A0[1-9][0-9]{0,3}'
        if True == is_include_hyphen:
            pattern += '-'
        pattern += '[0-9]{1,4}'
        if True == is_include_hyphen:
            pattern += '-'
        pattern += '[0-9]{4}\Z'
        return re.match(pattern, value) is not None
    def make_directory(file_path):
        """
        ディレクトリを作成する（makedirsのラッパー）
        """
        try:
            if False == os.path.isdir(file_path):
                os.makedirs(file_path)
        except FileExistsError as fee:
            # 同時に同名のディレクトリを作るアクセスがあった時のチェック用
            if False == os.path.isdir(file_path):
                # ディレクトリ作成に失敗
                return False
        return True
    def get_token(byte_length):
        """
        第三者が知り得ない秘密情報(トークン)の値を取得する
        """
        return secrets.token_hex(byte_length)
    def get_token_for_url(byte_length):
        """
        第三者が知り得ない秘密情報(トークン)の値を取得する（URL文字列用）
        """
        return secrets.token_urlsafe(byte_length)
    def get_unique_id():
        """
        ユニークなIDを取得する（推測可能なので注意）
        """
        return str(uuid.uuid4())
