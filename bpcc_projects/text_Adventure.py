import pickle

#Create class for rooms
class Room:
    def __init__(self, name, description, items=None, exits=None, winning_condition=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.exits = exits or {}
        self.winning_condition = winning_condition

    def __str__(self):
        return f"{self.name}\n{self.description}\n"
    
    # Method to check winning condition
    def check_winning_condition(self, player):
        if self.winning_condition:
            return self.winning_condition(player)
        return False    

#Create class for items with interaction for puzzle
class Item:
    def __init__(self, name, description, puzzle=None):
        self.name = name
        self.description = description
        self.puzzle = puzzle
    #Define item interaction for puzzle element
    def interact(self):
        if self.puzzle:
            while True:
                puzzle_answer = input('The screen asks, "What does the Cup of Stars symbolize?" ')
                if puzzle_answer.lower() == self.puzzle.lower():
                    print("The game reads, 'That's correct.  The locked room is the end of this story.  Use the map and key.'\n")
                    break
                else:
                    print("The game reads, 'No, that is not correct.'\n")

            
#Create player class for saving player backpack
class Player:
    def __init__(self):
        self.backpack = [Item("The Cup of Stars", "A cup symbolizing freedom.")]

#Define a separate function for winning condition
def room6_winning_condition(player):
    return any(item.name == "Key" for item in player.backpack)

#Create menu that lists options with numbers
def display_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

#Define how a game is saved 
def save_game(player, current_room):
    save_file = open("savegame.txt", "wb")
    pickle.dump((player, current_room, current_room.winning_condition), save_file)
    save_file.close()

#Define how a game is loaded
def load_game():
    try: 
        load_file = open("savegame.txt", "rb")
        loaded_data = pickle.load(load_file)
        load_file.close()

        player, current_room, loaded_winning_condition = loaded_data
        #Check if loaded data contains winning conditions
        if loaded_winning_condition:
            current_room.winning_condition = loaded_winning_condition
        else:
            current_room.winning_condition = None

        return player, current_room
    except FileNotFoundError:
        print("No saved game found.")
        return None
    

def main():
    #Intro Program
    print('**Johnny Moore - Text Adventure**')
    print('**CTEC 102-902**')
    print('')
    print('This is a text adventure game inspired by')
    print('"The Haunting of Hill House."')
    input('Press a key to open the front door of Hill House: ')

    print("\nWelcome to Hill House...\n")
    
    #Define rooms
    room1 = Room("**Toy Room**", "You are in Nellie's Toy Room. You see a dollhouse, curtains with pink tassels, \nand, on the floor, a cup with stars symbolizing freedom that you put in your backpack.\nThere are doors to the east and west.")
    room2 = Room("**Treehouse**", "You are in Luke's Treehouse.\nInexplicably, there is a tree fort in the middle of the room, and no exit but the door in which you came.", items=[Item("Key", "A key in the shape of a skull.")])
    room3 = Room("**Dance Studio**", "You are in Theo's Dance Studio.\nThe furniture is pushed to the walls leaving the floor mostly bare.", items=[Item("Paper", "It's a map that says 'from the beginning...W/N/W/S'")])
    room4 = Room("**Game Room**", "You are in Steven's Game Room. \nArcade cabinets are everywhere. ", items=[Item("Handheld Game", "There is text on the screen.", puzzle="freedom")])
    room5 = Room("**Family Room**", "You are in Shirley's Family Room. \nThere are books, a comfy couch, and a photo album.\nThere's a locked red door to the south.")
    room6 = Room("**Red Room**", "You have found the Red Room.  The walls are decaying and covered with black mold.  You are swallowed.", winning_condition=room6_winning_condition)

    #Connect rooms
    room1.exits = {"go east": room2, "go west": room3}
    room2.exits = {"go west": room1}
    room3.exits = {"go east": room1, "go north": room4}
    room4.exits = {"go south": room3, "go west": room5}
    room5.exits = {"go east": room4, "go south": room6}
    room6.exits = {"go north": room5}

    #Create instances of room and player classes
    current_room = room1
    player = Player()
    #Set game_running variable for loop
    game_running = True

    #run loop for exploring
    while game_running:
        # Check if in room6 and have key in backpack to win the game
        if current_room == room6:
            if any(item.name == "Key" for item in player.backpack):
                if current_room.winning_condition(player):
                    print(current_room)
                    print('You have completed the game. I am sorry for your fate. Thank you for playing.')
                    game_running = False
                    break  # Exit the loop after winning
            else:
                print("You need a key to enter this room.\n")
                current_room = room5
        elif current_room == room6 and current_room.winning_condition(player):
            print(current_room)
            print('You have completed the game. I am sorry for your fate. Thank you for playing.')
            game_running = False
            break  # Exit the loop after winning
        
        print(current_room)
        
        #Check for items in the room
        if current_room.items:
            print("Items in the room:")
            for item in current_room.items:
                print(f"- {item.name}\n")
            
            #Create loop for item pick up
            while True:
                item_action = input("Do you want to pick up the item? (Y or N): ")   
                if item_action.lower() == "y":
                    picked_item = current_room.items.pop() #take picked up item out of room
                    player.backpack.append(picked_item) #put picked up item in backpack
                    print(f"You picked up {picked_item.name}. {picked_item.description}\n")
                    picked_item.interact() #call item interact
                    break #Exit loop if user picks up item
                elif item_action.lower() == "n":
                    break  #Exit loop if user chooses not to pick up item
                else:
                    print("Invalid input. Try again.") #loops if user inputs incorrectly

        #display menu and ask for user input
        display_menu(list(current_room.exits.keys()) + ["check backpack", "save game", "load game", "quit"])
        action = input("What do you want to do next? ").lower()

        #Handle player input
        if action in current_room.exits:
            print('')
            current_room = current_room.exits[action]
        elif action == "check backpack":
            print("\nbackpack:")
            for item in player.backpack:
                print(f"- {item.name}. {item.description}\n")
        elif action == "quit":
            print("Thanks for playing!")
            game_running = False
        elif action == "save game":
            save_game(player, current_room)
            print("Game saved.\n")
        elif action == "load game":
            loaded_data = load_game()
            if loaded_data:
                player, current_room = loaded_data
                print('Game loaded.\n')
        else:
            print("Invalid input. Try again.\n")



    input('Press a key to exit: ')
            
if __name__ == "__main__":
    main()