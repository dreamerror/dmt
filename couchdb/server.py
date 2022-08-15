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

    def get_uuids(self, count: int = 10) -> List[str]:
        """
        Generate list of uuids that may be used as documents' _id fields
        :param count: Count of uuids that should be returned
        :return: List of uuids
        """
        uuids_url = self._url + f"_uuids?{count=}"
        response = self.session.get(uuids_url)
        return response.json()["uuids"]

    def __get_db(self, database: Database):
        """
        return True if database exists
        Authorization required
        """
        response = self.session.get(self._url + database.name)
        match response.status_code:
            case 404:
                raise exc.DatabaseDoesNotExist(database.name)
            case _:
                return True

    def __create_db(self, database: Database):
        """
        Create database in current node
        Authorization required
        """
        response = self.session.put(self._url + database.name)
        match response.status_code:
            case 400:
                raise exc.InvalidName(database.name)
            case 401:
                raise exc.NotAuthorised
            case 412:
                raise exc.DatabaseAlreadyExists(database.name)
        if database.docs:
            self.bulk_insert(database, database.docs)

    def get_or_create_db(self, database: Database):
        try:
            self.__get_db(database)
        except exc.DatabaseDoesNotExist:
            self.__create_db(database)

    def delete_db(self, database: Database):
        """
        Delete existing database
        Authorization required
        """
        response = self.session.delete(self._url + database.name)
        match response.status_code:
            case 400:
                raise exc.InvalidName(database.name)
            case 401:
                raise exc.NotAuthorised
            case 404:
                raise exc.DatabaseDoesNotExist(database.name)
            case _:
                return True

    def create_document(self, database: Database, document: Document):
        """
        Create document in existing database
        Authorization required
        """
        if "_id" not in document.keys():
            document["_id"] = self.get_uuids(1)[0]
        response = self.session.post(self._url + database.name, json=document.json)
        match response.status_code:
            case 400:
                raise exc.InvalidName(database.name)
            case 401:
                raise exc.NotAuthorised
            case 404:
                raise exc.DatabaseDoesNotExist(database.name)
            case 409:
                raise exc.ConflictingDocument(document["_id"])
            case _:
                return response.json()

    def bulk_insert(self, database: Database, docs: List[Document]):
        req_body = {"docs": list((doc.json for doc in docs))}
        response = self.session.post(self._url + database.name + "/_bulk_docs", json=req_body)
        match response.status_code:
            case 400:
                raise exc.InvalidData(req_body)
            case 404:
                raise exc.DatabaseDoesNotExist(database.name)

    def find_docs(self, database: Database, selector: Selector):
        response = self.session.post(self._url + database.name + "/_find", json=selector.json())
        return response.json()["docs"]
