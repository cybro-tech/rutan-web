import os

B_CONFIG = {
    'host': os.getenv('MYSQLHOST'),
    'port': int(os.getenv('MYSQLPORT', 3306)),
    'user': os.getenv('MYSQLUSER'),
    'password': os.getenv('MYSQLPASSWORD'),
    'database': os.getenv('MYSQLDATABASE')
}

SECRET_KEY = os.getenv('SECRET_KEY', 'rutan_secret')

UPLOAD_FOLDER = 'static/uploads'

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}
