import os

# Debug environment variable
DEBUG = True

# Application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Local DB
HOST = "127.0.0.1"
PORT = 3606
USERNAME = "root"
PASSWORD = "root"
DATABASE_NAME = "sregister"

SQLALCHEMY_DATABASE_URI = (
    "mysql+pymysql://"
    "{username}:{password}@{host}/{dbname}".format(
            username=USERNAME, password=PASSWORD,
            host=HOST, dbname=DATABASE_NAME
    )
)

SQLALCHEMY_TRACK_MODIFICATIONS = True

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = "a*#(!'!<S>?>:=-LA<lSD@!"

SECRET_KEY = "&!*#S<.,>,E-0oPQW??//CplQ{T}"

DOMAIN_NAME = "http://0.0.0.0:5000"
