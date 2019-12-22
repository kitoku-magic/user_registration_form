class config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = False
    PG_CHARACTER_SET = 'utf-8'

class testing(config):
    ENV = 'testing'
    TESTING = True

class development(config):
    ENV = 'development'
    DEBUG = True

class production(config):
    ENV = 'production'
    SESSION_COOKIE_SECURE = True
