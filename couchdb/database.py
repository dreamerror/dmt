from typing import List
from requests import Session

from couchdb import Document
from couchdb.utils import get_uuids
from couchdb.query import Selector
import couchdb.exceptions as exc


class Database:
    def __init__(self, name: str, session: Session, url: str):
        self.name = name
        self._session = session
        self.url = url

    def __repr__(self):
        return f"Database(\"{self.name}\")"

    async def _all_docs(self):
        response = self._session.post(self.url + f"{self.name}/_find", json={"selector": {}})
        return response.json()["docs"]

    @property
    async def docs(self):
        resp = await self._all_docs()
        for doc in resp:
            yield Document(**doc)

    def _get_doc_by_id(self, doc_id: str | int):
        response = self._session.get(self.url + f"{self.name}/{doc_id}")
        match response.status_code:
            case 400:
                raise exc.UnknownError
            case 404:
                raise exc.DocumentDoesNotExist(doc_id)
            case 401:
                raise exc.NotAuthorised
            case 200:
                return Document(**response.json())

    def delete_db(self):
        """
        Delete existing database
        Authorization required
        """
        response = self._session.delete(self.url + self.name)
        match response.status_code:
            case 400:
                raise exc.InvalidName(self.name)
            case 401:
                raise exc.NotAuthorised
            case 404:
                raise exc.DatabaseDoesNotExist(self.name)
            case _:
                return True

    def create_document(self, document: Document):
        """
        Create document in existing database
        Authorization required
        """
        if "_id" not in document.keys():
            document["_id"] = get_uuids(self.url, self._session, 1)[0]
        response = self._session.post(self.url + self.name, json=document.json)
        match response.status_code:
            case 400:
                raise exc.InvalidName(self.name)
            case 401:
                raise exc.NotAuthorised
            case 404:
                raise exc.DatabaseDoesNotExist(self.name)
            case 409:
                raise exc.ConflictingDocument(document["_id"])
            case _:
                return response.json()

    def bulk_insert(self, docs: List[Document]):
        req_body = {"docs": list((doc.json for doc in docs))}
        response = self._session.post(self.url + self.name + "/_bulk_docs", json=req_body)
        match response.status_code:
            case 400:
                raise exc.InvalidData(req_body)
            case 404:
                raise exc.DatabaseDoesNotExist(self.name)

    async def find_docs(self, selector: Selector):
        response = self._session.post(self.url + self.name + "/_find", json=selector.json())
        match response.status_code:
            case 400:
                pass  # невалидный реквест, нужно прописать эксепшн для этого
            case 401:
                raise exc.NotAuthorised
            case 404:
                raise exc.DatabaseDoesNotExist(self.name)
            case 500:
                pass  # ошибка при исполнении запроса, тоже нужен свой эксепшн
        return response.json()["docs"]

    def __getitem__(self, item_id):
        return self._get_doc_by_id(item_id)
