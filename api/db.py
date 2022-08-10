import settings
from couchdb import Couch
from models import DatabaseUser


user = DatabaseUser(username=settings.DB_USERNAME, password=settings.DB_PASSWORD)

server = Couch(settings.DB_HOST, settings.DB_PORT, user)
