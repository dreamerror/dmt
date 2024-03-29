class NotAuthorised(Exception):
    pass


class AuthorizationFailed(Exception):
    def __str__(self):
        return "Name or password is incorrect"


class InvalidName(Exception):
    """
    Only lowercase characters (a-z), digits (0-9), and any of the characters _, $, (, ), +, -, and / are allowed.
    Must begin with a letter.
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Name \"{self.name}\" is invalid. {self.__doc__}"


class InvalidData(Exception):
    def __init__(self, data: dict):
        self.data = data

    def __str__(self):
        return f"\"{self.data}\" is invalid JSON Data"


class DatabaseAlreadyExists(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Database \"{self.name}\" already exists"


class DatabaseDoesNotExist(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Database\"{self.name}\" does not exist"


class DocumentDoesNotExist(Exception):
    def __init__(self, doc_id: str | int):
        self.doc_id = doc_id

    def __str__(self):
        return f"Document with id<{self.doc_id}> does not exist"


class ConflictingDocument(Exception):
    def __init__(self, uuid: str):
        self.uuid = uuid

    def __str__(self):
        return f"Document with ID \"{self.uuid}\" already exists"


class UnknownError(Exception):
    pass
