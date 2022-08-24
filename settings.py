import os

import dotenv


dotenv.load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
JWT_SECRET = os.getenv("JWT_SECRET")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
JWT_EXPIRE_MINUTES = os.getenv("JWT_EXPIRE_MINUTES")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
