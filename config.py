import os

DB_CONFIG = {
    'host': os.environ['DB_HOST'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'database': os.environ['DB_NAME'],
    'port': int(os.environ['DB_PORT']),
}

SECRET_KEY = os.environ.get('SECRET_KEY', 'rutan_secret')

UPLOAD_FOLDER = 'static/uploads'

IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DOC_EXTENSIONS = {'pdf'}
