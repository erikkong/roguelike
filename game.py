import game_map
import tdl
my_map = game_map.my_map

#A game object, either a maincharacter or a key 
class GameObject:
    def __init__(self, x, y, char, color, objtype):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.objtype = objtype

    #Move the object
    def move(self, dx, dy):
        if not (my_map[self.x + dx][self.y + dy].blocked):
            self.x += dx
            self.y += dy
                       

    #Draw the object on screen
    def draw(self, con):
        con.draw_char(self.x, self.y, self.char, self.color)

    #Remove the character from screen
    def clear(self):
        con.draw_char(self.x, self.y, '', self.color, bg=None)

    #Converts the object to a string with all the attributes separated by '-'
    def __str__(self):
        string = str(self.x) + "-" + str(self.y) + "-" + str(self.char) + "-" + str(self.color) + "-" + str(self.objtype)
        return string

#Checks if the game has been won
def check_win():
    p1_in_position = player1.x == goal1.x and player1.y == goal1.y
    p2_in_position = player2.x == goal2.x and player2.y == goal2.y

    all_keys = (len(inventory1) == 2 and len(inventory2) == 2)
    return p1_in_position and p2_in_position and all_keys

        

#Create the players as gameobjects
player1 = GameObject(20, 23, '@', (255,255,255), 1)
player2 = GameObject(22, 24, '@', (255,255,0), 2)
key1 = GameObject(30, 10, 'P', (0,255,0), 3)
key2 = GameObject(40, 30, 'P', (88, 77, 20), 3)
key3 = GameObject(70, 18, 'P', (255, 0, 0), 3)
key4 = GameObject(15, 43, 'P', (150, 100, 255), 3)
goal1 = GameObject(19, 21, 'X', (255, 255, 255), 4)
goal2 = GameObject(20, 21, 'X', (255, 255, 0), 4)
inventory1 = []
inventory2 = []
objects = [player1, player2, key1, key2, key3, key4, goal1, goal2]

#Given the key press, handles the given command (this is done server side)
def handle_key(key, player):

    if player.objtype == 1:
        if key == 'UP':
            player.move(0,-1)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 2):
                    player.move(0,1)
                    
     
        elif key == 'DOWN':
            player.move(0,1)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 2):
                    player.move(0,-1)
     
        elif key == 'LEFT':             
            player.move(-1,0)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 2):
                    player.move(1,0)
     
        elif key == 'RIGHT':       
            player.move(1,0)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 2):
                    player.move(-1,0)   

        elif key == 'SPACE':
            if len(inventory1)<2:
                for obj in objects:
                    if obj.x == player.x and obj.y == player.y and (obj.objtype == 3):
                        objects.remove(obj)
                        inventory1.append(obj)
                       
    elif player.objtype == 2:
        if key == 'UP':
            player.move(0,-1)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 1):
                    player.move(0,1)
                    
     
        elif key == 'DOWN':
            player.move(0,1)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 1):
                    player.move(0,-1)
     
        elif key == 'LEFT':             
            player.move(-1,0)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 1):
                    player.move(1,0)
     
        elif key == 'RIGHT':       
            player.move(1,0)
            for obj in objects:
                if (obj.x == player.x and obj.y == player.y) and (obj.objtype == 1):
                    player.move(-1,0)   

        elif key == 'SPACE':
            if len(inventory2)<2:
                for obj in objects:
                    if obj.x == player.x and obj.y == player.y and (obj.objtype == 3):
                        objects.remove(obj)
                        inventory2.append(obj)

    if check_win():
        letter1 = GameObject(37, 47, 'W', (255, 255 ,0), 5)
        letter2 = GameObject(38, 47, 'I', (255, 255 ,0), 5)
        letter3 = GameObject(39, 47, 'N', (255, 255 ,0), 5)
        letter4 = GameObject(40, 47, 'N', (255, 255 ,0), 5)
        letter5 = GameObject(41, 47, 'E', (255, 255 ,0), 5)
        letter6 = GameObject(42, 47, 'R', (255, 255 ,0), 5)
        letter7 = GameObject(43, 47, '!', (255, 255 ,0), 5)
        objects.append(letter1)
        objects.append(letter2)
        objects.append(letter3)
        objects.append(letter4)
        objects.append(letter5)
        objects.append(letter6)
        objects.append(letter7)
        
