import secrets

class config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = secrets.token_hex(64)
    SESSION_COOKIE_SECURE = False

class testing(config):
    TESTING = True

class development(config):
    DEBUG = True

class production(config):
    SESSION_COOKIE_SECURE = True
