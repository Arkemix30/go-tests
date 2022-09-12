import os
import redis
from dotenv import load_dotenv

load_dotenv(override=True)

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USERNAME = os.environ.get('DB_USERNAME', 'default')
DB_PASSWORD = os.environ.get('DB_PASSWORD', None)
DB_PORT = os.environ.get('DB_PORT', "6379")
DB_NAME = os.environ.get('DB_NAME', 'default')


def get_db_connection():
    conn = redis.Redis.from_url(f"redis://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
    try:
        conn.ping()
    except Exception:
       raise ValueError('Could not connect to redis database')
    return conn
