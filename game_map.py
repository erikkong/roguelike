import global_variables
MAP_HEIGHT = global_variables.MAP_HEIGHT
MAP_WIDTH = global_variables.MAP_WIDTH

#A tile on the map
class Tile:
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
 
        
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

#SERVER
class Dungeon:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

#Creates the map
def make_map():
    global my_map
 
    #fill map with "blocked" tiles
    my_map = [[ Tile(True)
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]
 
    #Create all the dungeons for the map
    dungeon1 = Dungeon(0, 15, 10, 15)
    dungeon2 = Dungeon(15, 18, 10, 10)
    dungeon3 = Dungeon(0,2,20,8)
    dungeon4 = Dungeon(0,35,30,9)
    dungeon5 = Dungeon(40,35,15,4)
    dungeon6 = Dungeon(40,40,15,4)
    dungeon7 = Dungeon(65,34,10,10)
    dungeon8 = Dungeon(58,20,20,10)
    dungeon9 = Dungeon(34,26,20,7)
    dungeon10 = Dungeon(40,2,10,20)
    dungeon11 = Dungeon(25,4,10,10)
    dungeon12 = Dungeon(55,2,8,8)
    dungeon13 = Dungeon(66,11,12,8)
    create_dungeon(dungeon1)
    create_dungeon(dungeon2)
    create_dungeon(dungeon3)
    create_dungeon(dungeon4)
    create_dungeon(dungeon5)
    create_dungeon(dungeon6)
    create_dungeon(dungeon7)
    create_dungeon(dungeon8)
    create_dungeon(dungeon9)
    create_dungeon(dungeon10)
    create_dungeon(dungeon11)
    create_dungeon(dungeon12)
    create_dungeon(dungeon13)

#Creates a dungeon
def create_dungeon(dungeon):
    global my_map
    for x in range(dungeon.x1 + 1, dungeon.x2):
        for y in range(dungeon.y1 + 1, dungeon.y2):
            my_map[x][y].blocked = False
            my_map[x][y].block_sight = False


#Create a horizontal path between two dungeons
def create_x_path(x1, x2, y):
    global my_map
    for x in range(min(x1, x2), max(x1, x2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False

#Create a vertical path between two dungeons 
def create_y_path(y1, y2, x):
    global my_map
    for y in range(min(y1, y2), max(y1, y2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False


make_map()
#Create all the paths for the map
create_x_path(10, 18, 20)
create_x_path(10, 40, 20)
create_x_path(20, 40, 37)
create_x_path(20, 40, 42)
create_x_path(40, 65, 37)
create_x_path(40, 59, 42)
create_x_path(50, 58, 28)
create_x_path(20, 25, 6)
create_x_path(46, 70, 6)


create_y_path(6, 15, 2)
create_y_path(6, 19, 18)
create_y_path(20, 35, 6)
create_y_path(37, 42, 59)
create_y_path(30, 34, 68)
create_y_path(6, 12, 70)
