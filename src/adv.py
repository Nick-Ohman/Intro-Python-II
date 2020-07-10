from room import Room
from player import Player
from items import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



## create items

items = {
    "food": Item("Sherbet Lemon", "You might need food if you get lost"),
    "water": Item("Water", "You might be thirsty with all this walking"),
    "Light": Item("Light of Eärendil's star", "May it be a light to you in dark places, when all other lights go out."),
    "Sword": Item("sword of gondor", "Protection for yourself"),
    "goldpiece": Item("Gold Piece", "Found your first piece"),
    "helmate": Item("Chest Armour", "Protection")
}
room["foyer"].items = [items["goldpiece"], items["Light"]]
room["overlook"].items = [items["Sword"], items["food"]]
room["narrow"].items = [items["water"]]
room["treasure"].items = [items["water"]]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



# directions will ne N S E W

# follow step 1 define room

# after that take a name prompt
needhelp = ''' \n   How to play: \n\n, Type \'n\' to move north\n, Type \'s\' to move south\n, Type \'w\' to move west\n, Type \'e\' to move east\n, Type \'q\' at any time to quit\n     Type \'h\' for help '''


def start_game():
    player = Player(name = input('Enter name to start  '), current_room = room['outside'], items = [items["helmate"]])
    
    print(player)


    def grabdrop():
        choice = input(f'This room has:     {player.current_room.printitems()} \n         ')
        print(choice)
        if choice == 'ok':
            pass
        elif choice == 'get':
            player.getItem(f'{choice[5:]}')
        elif choice == 'drop':
            player.dropItem(f'{choice[6:]}')
        else:
            pass


    # while not(player.in_treasure):
    
    while not(player.in_treasure):
        gamer_input = input( "\nWhich direction would you like to move?  ")
        print('\n')
        if gamer_input == 'q':
            print('\n     !! Thanks for playing !!\n')
            exit()
        elif gamer_input == 'h':
            print(needhelp)
        elif gamer_input == 'n':
            try:
                player.current_room = player.current_room.n_to
                if player.current_room.name == "Treasure Chamber":
                    print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                    print('You have found the treasure')
                    won_game = input('Would you like to play again? Type y for yes, n for no...   ')
                    if won_game == 'w':
                        start_game()
                    else:
                        print('\n     !! Thanks for playing !!\n')
                        exit()
                else:
                    print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                    grabdrop()
                    gamer_input
            except:
                print("There is no room to the north")
                gamer_input
        elif gamer_input == 's':
            try:
                player.current_room = player.current_room.s_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                grabdrop()
                gamer_input                
            except:
                print('There is no room to the south.')
                gamer_input        
        elif gamer_input == 'e':
            try:
                player.current_room = player.current_room.e_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                grabdrop()

                gamer_input                 
            except: 
                print('There is no room to the east.')
                
        elif gamer_input == 'w':
            try:
                player.current_room = player.current_room.w_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                grabdrop()

                gamer_input
            except:
                print('There is no room to the west.')
                gamer_input                      

start_game()


    