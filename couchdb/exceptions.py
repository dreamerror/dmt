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


class DatabaseAlreadyExists(Exception):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Database \"{self.name}\" already exists"
