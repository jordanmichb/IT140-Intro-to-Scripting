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
    # Show current room.
    print("You are at the " + current_room + ".\n")
    # Display inventory.
    print("Inventory: {}\n".format(inventory)) 
    # Determines if room has an item.
    if 'Item' in rooms[current_room]:  
        # Determines if item has been picked up.
        if rooms[current_room]['Item'] not in inventory:  
            if current_room == 'Cave':
                # Use separate text for item starting with noun.
                print("You see an " + rooms[current_room]['Item'] + ".\n")  
            elif current_room == 'Waterfall':
                # Use separate text for plural item.
                print("You see some " + rooms[current_room]['Item'] + ".\n")  # separate text for plural item.
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
    
    # Start at campsite.
    current_room = 'Campsite'  
    # Call function.
    show_instructions()  
    
    # True for all rooms except clearing.
    while current_room != 'Clearing':
        # Call function.  
        show_status(current_room, inventory, rooms)
        # Normalize input so program reads any caps combo and matches dict.
        command = input('Enter a command: ').title()  
        print("--------------------------------------")
        # Determines if command is to pick up item.
        if command.startswith("Get"):  
            # Determines if command refers to any item already retrieved, excludes 'Get '.
            if command[4:] in inventory:  
                print("You already have that!\n")
                # Disallows extra input characters after item
            elif command[4:] == rooms[current_room]['Item']:  
                # Add item.
                inventory.append(rooms[current_room]['Item'])  
                print(rooms[current_room]['Item'], "retrieved!\n")
            else:
                print("Can't " + command.lower() + ".\n")
        # Determines if command is to move rooms.
        elif command in rooms[current_room]:  
            # Updates room if valid command.
            current_room = rooms[current_room][command]  
        else:
            print("You can't do that!\n")

    if current_room == 'Clearing':
        # If player did not collect all items.
        if len(inventory) < 6:  
            print("You have made it to the clearing at the edge of the woods...\n")
            print("You see the Wendigo, and the Wendigo sees you...\n")
            print("You frantically search your pockets and realize you are missing supplies!\n")
            print("The Wendigo has killed you.")
        # If player collected all items.
        elif len(inventory) == 6:  
            print("You have made it to the clearing at the edge of the woods...\n")
            print("You see the Wendigo, and the Wendigo sees you...\n")
            print("You gathered all the supplies and were able to defeat the Wendigo!\n")
            print("You have made it out safely.")


main()
