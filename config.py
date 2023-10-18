import os

main_dir = os.path.dirname(os.path.abspath(__file__))

# Production Antiguo
URL_HOME = "http://172.16.78.83:5000/"
# URL_GLOBAL = "http://172.16.78.83:8000/"

# Production Nuevo
# URL_HOME = "http://172.16.83.23:5000/"
# URL_GLOBAL = "http://172.16.83.23:8000/api_fastq/"

# Develop Adria
# URL_HOME = "http://172.16.82.47:5000"
# URL_GLOBAL = "http://172.16.82.47:8000/api_fastq/"

# Develop Alex
# URL_HOME = "http://172.16.82.45:5000/"
# URL_GLOBAL = "http://172.16.82.45:8000/api_fastq/"


class Config(object):
    SECRET_KEY = "lablam.2017"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://db_user:db_pass@prod_host:port/db_name"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://db_user:db_pass@dev_host:port/db_name"


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@test_host:port/db_name'


class Config_Files(object):
    UPLOADS = "app/data"
    WORKING_DIRECTORY = "/"
    MAX_CONTENT_LENGHT = 50 * 1024 * 1024
    ALLOWED_EXTENSIONS = {"csv", "xlsx", "xls"}
    SEND_FILE_MAX_AGE_DEFAULT = 5
