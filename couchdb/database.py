from typing import List

from couchdb.document import Document


class Database:
    def __init__(self, name: str, documents: List[Document] | None = None):
        self.name = name
        self.docs = documents if documents is not None else list()

    def __repr__(self):
        return f"Database(\"{self.name}\")"

    def add_doc(self, document: Document):
        self.docs.append(document)
