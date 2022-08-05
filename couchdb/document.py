class Document:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setitem__(self, key: str, value):
        self.__dict__[key] = value

    def __getitem__(self, key: str):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        attrs = ", ".join([f"{key}: {value}" for key, value in self.items()])
        return f"<{self.__class__.__name__}>: ({attrs})"
