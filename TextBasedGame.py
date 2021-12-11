# Jordan Ballard
def show_instructions():
    print("\nWelcome to the Wendigo Text Adventure Game!\n")
    print("Collect all six items before you face the Wendigo, or risk being killed.\n")
    print("To move to a new location, type: 'north', 'south', 'east', or 'west'\n")
    print("To pick up an item, type: 'get [insert item name]'")
    print("--------------------------------------")
    print("START")
    print("--------------------------------------")


def show_status(current_room, inventory, rooms):
    print("You are at the " + current_room + ".\n")  # show current room
    print("Inventory: {}\n".format(inventory))  # display inventory
    if 'Item' in rooms[current_room]:  # determines if room has an item
        if rooms[current_room]['Item'] not in inventory:  # determines if item has been picked up
            if current_room == 'Cave':
                print("You see an " + rooms[current_room]['Item'] + ".\n")  # separate text for item starting with noun
            elif current_room == 'Waterfall':
                print("You see some " + rooms[current_room]['Item'] + ".\n")  # separate text for plural item
            else:
                print("You see a " + rooms[current_room]['Item'] + ".\n")


def main():
    inventory = []  # begin with empty inventory
    rooms = {
        'Campsite': {'North': 'Cliff', 'South': 'Riverbank', 'East': 'Redwood Grove', 'West': 'Fire Pit'},
        'Cliff': {'South': 'Campsite', 'East': 'Cave', 'Item': 'Firearm'},
        'Riverbank': {'North': 'Campsite', 'East': 'Waterfall', 'Item': 'Flint'},
        'Redwood Grove': {'North': 'Clearing', 'West': 'Campsite', 'Item': 'Satellite Radio'},
        'Fire Pit': {'East':  'Campsite', 'Item': 'Winter Jacket'},
        'Cave': {'West': 'Cliff', 'Item': 'Enchanted Medallion'},
        'Waterfall': {'West': 'Riverbank', 'Item': 'Silver Bullets'},
        'Clearing': {'South': 'Redwood Grove'}
    }

    current_room = 'Campsite'  # start at campsite

    show_instructions()  # call function

    while current_room != 'Clearing':  # true for all rooms except clearing
        show_status(current_room, inventory, rooms)  # call function
        command = input('Enter a command: ').title()  # normalize input so program reads any caps combo and matches dict
        print("--------------------------------------")
        if command.startswith("Get"):  # determines if command is to pick up item
            if command[4:] in inventory:  # determines if command refers to any item already retrieved, excludes 'Get '
                print("You already have that!\n")
            elif command[4:] == rooms[current_room]['Item']:  # disallows extra input characters after item
                inventory.append(rooms[current_room]['Item'])  # add item
                print(rooms[current_room]['Item'], "retrieved!\n")
            else:
                print("Can't " + command.lower() + ".\n")
        elif command in rooms[current_room]:  # determines if command is to move rooms
            current_room = rooms[current_room][command]  # updates room if valid command
        else:
            print("You can't do that!\n")

    if current_room == 'Clearing':
        if len(inventory) < 6:  # if player did not collect all items
            print("You have made it to the clearing at the edge of the woods...\n")
            print("You see the Wendigo, and the Wendigo sees you...\n")
            print("You frantically search your pockets and realize you are missing supplies!\n")
            print("The Wendigo has killed you.")
        elif len(inventory) == 6:  # if player collected all items
            print("You have made it to the clearing at the edge of the woods...\n")
            print("You see the Wendigo, and the Wendigo sees you...\n")
            print("You gathered all the supplies and were able to defeat the Wendigo!\n")
            print("You have made it out safely.")


main()
