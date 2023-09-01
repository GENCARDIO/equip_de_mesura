import os

main_dir = os.path.dirname(os.path.abspath(__file__))


class Config_Arxius(object):
    UPLOADS = "app/data"
    WORKING_DIRECTORY = "/"
    MAX_CONTENT_LENGHT = 50 * 1024 * 1024
    ALLOWED_EXTENSIONS = {"csv", "xlsx", "xls"}
    SEND_FILE_MAX_AGE_DEFAULT = 5
