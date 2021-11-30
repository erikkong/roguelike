import global_variables
import tdl
import game_map

my_map = game_map.my_map

MAP_WIDTH = global_variables.MAP_WIDTH
MAP_HEIGHT = global_variables.MAP_HEIGHT


#Colors for the map
color_dark_wall = (0, 0, 100)
color_dark_ground = (50, 50, 150)

#Attributes of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#Creates a "session"
tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
tdl.setFPS(LIMIT_FPS)

#Draws an object
def draw_object(obj):
    con.draw_char(obj.x, obj.y, obj.char, obj.color, bg=color_dark_ground)

#Renders the map
def render_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = my_map[x][y].block_sight
            if wall:
                con.draw_char(x, y, ' ', fg=None, bg=color_dark_wall)
            else:
                con.draw_char(x, y, ' ', fg=None, bg=color_dark_ground)

#Render all the graphics
def render_all(objects):
    render_map()            #Render the map without objects
    tdl.flush()             #Update screen
    
    #Render the objects
    for i in range(len(objects), 0, -1):     #For every object
        draw_object(objects[i-1])    #Render it

    root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0) #Update window
    tdl.flush()             #Update screen
    
