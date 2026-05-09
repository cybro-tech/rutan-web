import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

SECRET_KEY = os.getenv('SECRET_KEY', 'kunci_rahasia_rutan_makassar')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'static/uploads')

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}