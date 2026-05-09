import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', os.getenv('MYSQLHOST', 'localhost')),
    'user': os.getenv('DB_USER', os.getenv('MYSQLUSER', 'root')),
    'password': os.getenv('DB_PASSWORD', os.getenv('MYSQLPASSWORD', '')),
    'database': os.getenv('DB_NAME', os.getenv('MYSQLDATABASE', 'railway')),
    'port': int(os.getenv('DB_PORT', os.getenv('MYSQLPORT', 3306))),
}

SECRET_KEY = os.getenv('SECRET_KEY', 'rutan_secret')

UPLOAD_FOLDER = 'static/uploads'

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}
