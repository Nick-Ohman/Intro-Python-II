class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def ___str___(self):
        return f'{self.name}, {self. description}'