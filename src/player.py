# Write a class to hold player information, e.g. what room they are in
# currently.


## refer to GP

class Player:
    def __init__(self, name, current_room, items, in_treasure=False):
        self.name = name
        self.current_room = current_room
        self.in_treasure = in_treasure
        self.items = items


    def __str__(self):
        return f"          \nWelcome {self.name}, You're currently in {self.current_room.name}, {self.current_room.description}."


    def printitems(self):
        # for item in self.items:
        #     return item
        inventory = []
        for item in self.items:
            inventory.append(item.name)
        return inventory
    def getItem(self, item):
        selection = item
        self.items.append(selection)
    def dropItem(self, item):
        selection = item
        self.items.remove(selection)
        self.current_room.items.append(selection)