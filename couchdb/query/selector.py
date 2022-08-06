class SelectorElement:
    def __init__(self, field_name: str):
        self.field_name = field_name
        self.query = {field_name: dict()}

    def __lt__(self, other):
        self.query[self.field_name]["$lt"] = other

    def __le__(self, other):
        self.query[self.field_name]["$lte"] = other

    def __eq__(self, other):
        self.query[self.field_name]["$eq"] = other

    def __gt__(self, other):
        self.query[self.field_name]["$gt"] = other

    def __ge__(self, other):
        self.query[self.field_name]["$gte"] = other

    def __ne__(self, other):
        self.query[self.field_name]["$ne"] = other

    def __repr__(self):
        return repr(self.query)


class Selector:
    def __init__(self):
        self.expr = dict()
        self.elements = list()
        self.checked_elements = list()

    def add_elements(self, *args: SelectorElement):
        self.elements += args

    @property
    def expression(self):
        #  TODO: подумать, можно ли это как-то ускорить и нужно ли вообще
        for elem in self.elements:
            if elem not in self.checked_elements:
                self.checked_elements.append(elem)
                self.expr.update(elem.query)
        return {"selector": self.expr}

    def __repr__(self):
        return repr(self.expression)

    def json(self):
        return self.expression

