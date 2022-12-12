
#Jonathan Sladish

#A dictionary for the Hunter vs Bear text game
#The dictionary links a room to other rooms.
rooms = {
    'Cave One':
        {'South':'Cave Three','East':'Cave Two','Item':'Rabbit'},
    'Cave Two':{'West':'Cave One','Item':'Water'},
    'Cave Three':{'North':'Cave One','South':'Cave Four'},
    'Cave Four':{'North':'Cave Three','South':'Cave Seven','West':'Cave Six','East':'Cave Five', 'Item':'Deer'},
    'Cave Five':{'West':'Cave Four','South':'Cave Eight','Item':'Potatoes'},
    'Cave Six':{'East':'Cave Four','Item':'Bear'},
    'Cave Seven':{'East':'Cave Eight','North':'Cave Four','Item':'Carrots'},
    'Cave Eight':{'West':'Cave Seven','Item':'Apples'}
    }
#this is the start the game location and the method that allow an object to change
state = 'Cave One'
#this will define get new state: state and direction function
def get_new_state(state, direction):
# this say new state equal to state
    new_state = state
# this for loop statement hold the temporary integer for rooms
    for i in rooms:
# this if statement says temporary integer is equal to state
        if i == state:
# this if statement for direction in rooms temporary integer
            if direction in rooms[i]:
# this says new location is equal to rooms temporary integer and direction assigning new state
                new_state=rooms[i][direction]
#this will return the new location
    return new_state
# this will define get item location then try
def get_item(state):
    try:
#this will return rooms state and item value
        return rooms[state]['Item']
# this works with the try clause and return the condition statement value
    except:
        return '0'
#this define show instructions for the game and then print out each statement
def show_instructions():
    print("Hunter vs Bear Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the Bear.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
#this holds the value for show instructions
show_instructions()
#this holds the value for inventory
inventory=[]
#this while statement says helps repeat the printed statements for game play
while (1):
    print('You are in ', state)
    print('Inventory:',inventory)
    item=get_item(state)
#this if statement item sees item
    if item!='0':
#this prints the you see an item
        print('You see a',item)
#this if statement is equal to Bear then your eaten game over and ends game with exit
        if item == 'Bear':
            print('Crunch Crunch...GAME OVER!')
            exit(0)
# This says for direction input the value with printed enter your move
    direction = input('Enter your move: ')
# this if statement direction is eqaul to the directions east, west, north and south
    if (direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South'):
# this says direction equals direction and added slicing
        direction=direction[3:]
## new state is equal to get new state and then the state and direction
        new_state = get_new_state(state, direction)
# this if statement say if new location equals to location then print out the statement value
        if new_state == state:
            print('You can not go that direction enter other direction!')
# this else statement says location equal to new location changing the value
        else:
            state = new_state
# this else if statement says direction equals to string get the plus item
    elif direction==str('get '+item):
# this if statement for item in inventory will print out item statement value
        if item in inventory:
            print('Item already taken go to another room!!')
#this else statement inventory append the item
        else:
            inventory.append(item)
#if else statement direction slicing indexing is equal to get
    elif direction[0:4]=="get ":
# this prints can't get plus the direction with slicing index
        print("can't get "+direction[4:])
#else statement print invalid direction
    else:
        print("Invalid direction!")
#if statement length inventory 6 items found then print congratulations you won
    if len(inventory) == 6:
        print('Congratulations! You have collected all items and beaten the Bear!')
 # exit will end the game
        exit(0)