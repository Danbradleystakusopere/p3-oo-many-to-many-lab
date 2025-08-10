class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        from contract import Contract
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        from contract import Contract
        return [c.author for c in self.contracts()]
