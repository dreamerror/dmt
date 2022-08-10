import os

from dotenv import load_dotenv


load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
JWT_EXPIRE_MINUTES = os.getenv("JWT_EXPIRE_MINUTES")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
