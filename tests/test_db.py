from couchdb import Couch, Database, Document
from settings import DB_USERNAME, DB_PASSWORD


class TestCouch:
    SERVER = Couch()
    SERVER.authorize(DB_USERNAME, DB_PASSWORD)

    def test_create_db(self):
        new_db = Database("new_db")
        assert self.SERVER.create_db(new_db) is True
        self.SERVER.delete_db(new_db)

    def test_create_document(self):
        new_db = Database("new_db")
        new_doc = Document(number=123, string="123", arr=[1, 2, 3])
        assert new_doc["number"] == 123
        assert new_doc["arr"] == [1, 2, 3]
        self.SERVER.create_db(new_db)
        assert self.SERVER.create_document(new_db, new_doc)["ok"] == True
        self.SERVER.delete_db(new_db)