import settings
from couchdb import Couch
from models import DatabaseUser

if all((settings.DB_USERNAME is not None, settings.DB_PASSWORD is not None)):
    user = DatabaseUser(username=settings.DB_USERNAME, password=settings.DB_PASSWORD)
    server = Couch(settings.DB_HOST, settings.DB_PORT, user)
else:
    server = Couch(settings.DB_HOST, settings.DB_PORT)

