import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST') or os.getenv('MYSQLHOST', 'localhost'),
    'user': os.getenv('DB_USER') or os.getenv('MYSQLUSER', 'root'),
    'password': os.getenv('DB_PASSWORD') or os.getenv('MYSQLPASSWORD', ''),
    'database': os.getenv('DB_NAME') or os.getenv('MYSQLDATABASE', 'rutan_db'),
    'port': int(os.getenv('DB_PORT') or os.getenv('MYSQLPORT', 3306)),
}

SECRET_KEY = os.getenv('SECRET_KEY', 'kunci_rahasia_rutan_makassar')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}