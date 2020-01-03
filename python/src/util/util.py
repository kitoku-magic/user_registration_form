import dns.resolver

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
