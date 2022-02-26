##################
#Name: Angel Beltran
#Date: 2/17/2022
#Description: Room Adventure
#######################

from thedeath import death


#the blueprint for a room
class Room(object):
    # the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)
    def addItems(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self,item):
        # append the item to the list
        self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
    def delGrabbable(self, item):
        #removes the item from the list
        self.grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        #first, the room name
        s = f"You are in {self.name}"

        #next the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"

        #next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s
########## creates the rooms
def createRooms():
    # r1 through r4 are the four rooms in the mansion
    #current room is the room the player is currently in
    #since the currentRoom needs to be changed in the main part of the prorgam
    #it must be global
    global currentRoom

    r1 = Room("Room 1 ")
    r2 = Room("Room 2 ")
    r3 = Room("Room 3 ")
    r4 = Room("Room 4 ")

    # adds exit room 1
    r1.addExit("east", r2) # -> to the east room 1 is room 2
    r1.addExit("south", r3)

    # add grabbables to room 1
    r1.addGrabbable("key")

    #add items in room
    r1.addItems("chair", "It is made of wicker and no one is sitting on it")
    r1.addItems("table", "It is made of oak. A golden key rests upon it")

    #add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)

    #add items to room 2
    r2.addItems("rug", "It is nice and indian. It also needs to be vaccumed.")
    r2.addItems("fireplace", "It is full of ashes")

    #add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)

    #add grabbables to room 3
    r3.addGrabbable("book")

    #add items to room 3
    r3.addItems("bookshelves", "they are empty. Go figure")
    r3.addItems("statue", "There is nothing special about it")
    r3.addItems("desk", "The statue is resting on it. So is the book")

    #add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None) #Death!

    #add grabbables in room 4
    r4.addGrabbable("6-pack")

    #add items to room 4
    r4.addItems("soda_making_machine","Gourd is making some sort of soad on the soda making machine. A 6-pack is resting beside it")

    #set room 1 as the current room at the begining of the game
    currentRoom = r1


##########Start the ga
# me##########

inventory = []  # nothing in inventory yet
createRooms()  #create the room

while True:
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = f"{currentRoom}\n You are carrying {inventory}\n"

# if the current room is None, then the player is dead
# this only happens if the player goes south when in room 4
# exit the game
    if currentRoom == None:
        death()
        break
    #display status
    print("=================================================")
    print(status)

    #prompt the player for input
    action = input("What to do? ")

    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()
    #checks to see if the player wants to leave
    if (action == "quit" or action == "exit" or action == "bye"):
        break
    response = "I don't understand. Try Verb noun. Valid verbs are go, look, and take"

    #split the user into words

    words = action.split()

    #the game only understands two word input
    if len(words) == 2:
        #isolate the verb and noun
        verb = words[0]
        noun = words[1]

        #if the verb is go
        if verb == "go":
            # set a default response
            response = "Invalid exit"

            #check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                #a valid exit is found
                if noun == currentRoom.exits[i]:
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]

                    #set response (succes)
                    response = "Room change"
                    break

        elif verb == "look":
            #set a default response
            response = "I don't see that item"

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                if noun == currentRoom.items[i]:
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]

                    # no need to check any more items
                    break

        # if verb is: take
        elif verb == "take":
            response = "I don't see that item"

            #check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable items is found
                if noun == grabbable:
                    # add the grabbable  item to the player's
                    # inventory
                    inventory.append(grabbable)

                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)
                    #set the response (success)
                    response = "Item grabbed"
                    #no need to check for more grabbables
                    break

    #display the response
    print(f"\n{response}")














