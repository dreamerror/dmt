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
        self.expression = {"selector": dict()}
        self.elements = list()

    def add_elements(self, *args: SelectorElement):
        self.elements += args

    def __repr__(self):
        #  TODO: подумать, можно ли это ускорить, и нужно ли вообще
        expr = dict()
        for elem in self.elements:
            expr.update(elem.query)
        self.expression["selector"] = expr
        return repr(self.expression)

