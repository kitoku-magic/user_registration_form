import dns.resolver
import re

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
