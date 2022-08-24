from couchdb import Couch, Database, Document
from settings import DB_USERNAME, DB_PASSWORD


class TestCouch:
    SERVER = Couch()
    SERVER.authorize(DB_USERNAME, DB_PASSWORD)

    def test_create_db(self):
        assert isinstance(self.SERVER.get_or_create_db("new_db"), Database)
        new_db = self.SERVER.get_or_create_db("new_db")
        new_db.delete_db()

    def test_create_document(self):
        new_doc = Document(number=123, string="123", arr=[1, 2, 3])
        assert new_doc["number"] == 123
        assert new_doc["arr"] == [1, 2, 3]
        new_db = self.SERVER.get_or_create_db("new_db")
        assert new_db.create_document(new_doc)["ok"] is True
        new_db.delete_db()
