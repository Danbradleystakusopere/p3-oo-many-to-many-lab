class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        from contract import Contract
        return [c for c in Contract.all if c.author == self]

    def books(self):
        from contract import Contract
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        from contract import Contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        from contract import Contract
        return sum(c.royalties for c in self.contracts())
