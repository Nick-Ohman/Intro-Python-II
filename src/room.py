# Implement a class to hold room information. This should have name and
# description attributes.



## refer to GP


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.name}, {self.description}" 


    def printitems(self):
        inventory = []
        for item in self.items:
            inventory.append(item.name)
        return inventory