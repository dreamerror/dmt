from typing import List
from requests import Session

from couchdb.document import Document


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
