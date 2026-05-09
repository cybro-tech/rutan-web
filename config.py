import os

DB_CONFIG = {
    'host': os.environ['MYSQLHOST'],
    'user': os.environ['MYSQLUSER'],
    'password': os.environ['MYSQLPASSWORD'],
    'database': os.environ['MYSQLDATABASE'],
    'port': int(os.environ['MYSQLPORT']),
}

SECRET_KEY = os.environ.get('SECRET_KEY', 'rutan_secret')

UPLOAD_FOLDER = 'static/uploads'

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}
