# Write a class to hold player information, e.g. what room they are in
# currently.


## refer to GP

class Player:
    def __init__(self, name, current_room, in_treasure=False):
        self.name = name
        self.current_room = current_room
        self.in_treasure = in_treasure
        


    def __str__(self):
        return f"          \nWelcome {self.name}, You're currently in {self.current_room.name}, {self.current_room.description}."