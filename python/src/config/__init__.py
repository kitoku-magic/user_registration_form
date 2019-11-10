class config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = False
    PG_CHARACTER_SET = 'utf-8'

class testing(config):
    TESTING = True

class development(config):
    DEBUG = True

class production(config):
    SESSION_COOKIE_SECURE = True
