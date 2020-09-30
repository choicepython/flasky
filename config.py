import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.cooglemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_ISERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMYU_DATABASE_URL = os.environ.get('SQLALCHEMYU_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir
                                                                                                         ,
                                                                                                         'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMYU_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir
                                                                                                  , 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMYU_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
