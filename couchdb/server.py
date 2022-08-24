import requests
from typing import List
from datetime import datetime, timedelta

from couchdb.database import Database
from couchdb.document import Document
from couchdb.query import Selector
from models import DatabaseUser
import couchdb.exceptions as exc


class Couch:
    def __init__(self, db_host: str = "localhost", db_port: str | int = 5984, user: DatabaseUser | None = None):
        if not db_host.startswith("http"):
            db_host = "http://" + db_host
        self._url = f"{db_host}:{db_port}/"
        self.session = requests.Session()
        if user is not None:
            self.authorize(user.username, user.password)

    def authorize(self, username: str, password: str):
        """
        Make your CouchDB session authorized
        :param username: Your CouchDB name
        :param password: Your CouchDB password
        :return: True if authorization was successful
        """
        body = {
            "name": username,
            "password": password
        }
        response = self.session.post(self._url + "_session", data=body)
        if response.status_code == 401:
            raise exc.AuthorizationFailed
        for cookie in response.cookies:
            if cookie.name == "AuthSession":
                cookie.expires = datetime.timestamp(datetime.fromtimestamp(cookie.expires) + timedelta(days=180))
        return True

    def __get_db(self, database: str) -> Database:
        """
        return True if database exists
        Authorization required
        """
        response = self.session.get(self._url + database)
        match response.status_code:
            case 404:
                raise exc.DatabaseDoesNotExist(database)
        return Database(database, self.session, self._url)

    def __create_db(self, database: str) -> Database:
        """
        Create database in current node
        Authorization required
        """
        response = self.session.put(self._url + database)
        match response.status_code:
            case 400:
                raise exc.InvalidName(database)
            case 401:
                raise exc.NotAuthorised
            case 412:
                raise exc.DatabaseAlreadyExists(database)
        return Database(database, self.session, self._url)

    def get_or_create_db(self, database: str) -> Database:
        try:
            return self.__get_db(database)
        except exc.DatabaseDoesNotExist:
            return self.__create_db(database)
