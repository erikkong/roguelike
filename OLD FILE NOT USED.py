import tdl

#CLIENT
#Initialize graphics 
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
tdl.setFPS(LIMIT_FPS)

#SERVER
#A game object, either a maincharacter or a key 
class GameObject:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    #Move the object
    def move(self, dx, dy):
        if not my_map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy
            
    #Draw the object on screen
    def draw(self):
        con.draw_char(self.x, self.y, self.char, self.color)

    #Remove the character from screen
    def clear(self):
        con.draw_char(self.x, self.y, '', self.color, bg=None)

#SERVER
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

#SERVER
def make_map():
    global my_map
 
    #fill map with "blocked" tiles
    my_map = [[ Tile(True)
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]
 

    dungeon1 = Dungeon(20, 15, 10, 15)
    dungeon2 = Dungeon(50, 15, 10, 15)
    create_dungeon(dungeon1)
    create_dungeon(dungeon2)

#SERVER
def create_dungeon(dungeon):
    global my_map
    for x in range(dungeon.x1 + 1, dungeon.x2):
        for y in range(dungeon.y1 + 1, dungeon.y2):
            my_map[x][y].blocked = False
            my_map[x][y].block_sight = False

#SERVER
#Create a horizontal path between two dungeons
def create_x_path(x1, x2, y):
    global my_map
    for x in range(min(x1, x2), max(x1, x2) + 1):
        my_map[x][y].blocked = False
        my_map[x][y].block_sight = False


#CLIENT AND SERVER
#Get player input and move the character
def handle_keys():
    global player
    user_input = tdl.event.key_wait()
    con.draw_char(player.x, player.y, ' ', bg=None)
    if user_input.key == 'UP':
        player.move(0,-1)
 
    elif user_input.key == 'DOWN':
        player.move(0,1) 
 
    elif user_input.key == 'LEFT':
        player.move(-1,0)
 
    elif user_input.key == 'RIGHT':
        player.move(1,0)

    render_all()
    root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
    tdl.flush()

#CLIENT
#Render all the graphics
def render_all():
    #Render the objects
    for obj in objects:
        obj.draw()
        
    #Render the map
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = my_map[x][y].block_sight
            if wall:
                con.draw_char(x, y, None, fg=None, bg=color_dark_wall)
            else:
                con.draw_char(x, y, None, fg=None, bg=color_dark_ground)

#SERVER
#Create the players as gameobjects
player = GameObject(25, 23, '@', (255,255,255))
npc = GameObject(26, 24, '@', (255,255,0))
objects = [npc, player]

#CLIENT
#Graphics for the map
MAP_WIDTH = 80
MAP_HEIGHT = 45
color_dark_wall = (0, 0, 100)
color_dark_ground = (50, 50, 150)

#SERVER
make_map()
my_map[30][22].blocked = True
my_map[30][22].block_sight = True
my_map[50][22].blocked = True
my_map[50][22].block_sight = True
create_x_path(25, 55, 29)

#SERVER
#Main Game Loop
while not tdl.event.is_window_closed():
    render_all()
    root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
    tdl.flush()
    handle_keys()

