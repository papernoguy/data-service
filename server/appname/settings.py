import tempfile

db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = "REPLACE ME"


class ProdConfig(Config):
    SERVER_NAME = "replace me"
    ENV = "prod"
    MONGO_DATABASE_URI = "mongodb://127.0.0.1:27017/my_db"

    CACHE_TYPE = "simple"


class DevConfig(Config):
    SERVER_NAME = "localhost:5000"
    ENV = "dev"
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MONGO_DATABASE_URI = "mongodb://127.0.0.1:27017/my_db"

    CACHE_TYPE = "null"
    ASSETS_DEBUG = True


class TestConfig(Config):
    SERVER_NAME = "localhost:5000"
    ENV = "test"
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    MONGO_DATABASE_URI = "mongodb://127.0.0.1:27017/my_db"

    CACHE_TYPE = "null"
    WTF_CSRF_ENABLED = False
