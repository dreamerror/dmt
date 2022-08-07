from couchdb.query import Selector


class Index:
    def __init__(self, name: str):
        self.name = name
        self.index = {"name": name, "type": "json"}
        self.fields = set()

    def add_fields(self, *args: str):
        self.fields.update(set(args))

    def add_selector(self, selector: Selector):
        self.index["partial_filter_selector"] = selector.json()

    @property
    def expression(self) -> dict:
        self.index["fields"] = self.fields
        return self.index

