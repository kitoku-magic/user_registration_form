import logging

class config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = False
    LOG_MAX_BYTES = 100000
    LOG_BACKUP_COUNT = 10
    LOG_LEVEL = logging.DEBUG
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
    LOG_BACKUP_COUNT = 100
    LOG_LEVEL = logging.INFO
