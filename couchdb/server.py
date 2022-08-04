import requests
from typing import List

from database import Database
from document import Document
import couchdb.exceptions as exc


class Couch:
    def __init__(self, db_url: str = "http://localhost:5984/"):
        """
        :param db_url: URL used for connection to CouchDB
        """
        self._url = db_url
        if not db_url.endswith("/"):
            self._url += "/"
        self.session = requests.Session()

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

    def get_db(self, database: Database):
        response = self.session.get(self._url + database.name)
        return response.json()

    def create_db(self, database: Database):
        response = self.session.put(self._url + database.name)
        match response.status_code:
            case 400:
                raise exc.InvalidName(database.name)
            case 401:
                raise exc.NotAuthorised
            case 412:
                raise exc.DatabaseAlreadyExists(database.name)
            case _:
                return True

    def delete_db(self, database: Database):
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
        if "_id" not in document.data.keys():
            document.data["_id"] = self.get_uuids(1)[0]
        response = self.session.post(self._url + database.name, data=document.data)
        match response.status_code:
            case 400:
                raise exc.InvalidName(database.name)
            case 401:
                raise exc.NotAuthorised
            case 404:
                raise exc.DatabaseDoesNotExist(database.name)
            case 409:
                raise exc.ConflictingDocument(document.data["_id"])
            case _:
                return True
