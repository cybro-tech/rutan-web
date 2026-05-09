import os

DB_CONFIG = {
    'host': os.environ.get('MYSQLHOST'),
    'user': os.environ.get('MYSQLUSER'),
    'password': os.environ.get('MYSQLPASSWORD'),
    'database': os.environ.get('MYSQLDATABASE'),
    'port': int(os.environ.get('MYSQLPORT', 3306)),
}

SECRET_KEY = os.environ.get('SECRET_KEY', 'rutan_secret')
UPLOAD_FOLDER = 'static/uploads'

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}
