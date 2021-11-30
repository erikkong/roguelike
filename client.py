import socket               #To handle the transmission of data
import global_variables     #Variables such as port number and the socket

import tdl                  #The library used to make the game
import graphics             #The file to do with updating graphics and such
import game                 #The mechanics of the game (in this case it is only used for converting strings to renderable objects)

import threading            #To run things in parallel

#Converts a string matching a tuple to a tuple
def string_to_tuple(t):
    t = t.replace("(", "")                                          #Remove '(' resulting in t = 'r, g, b)'
    t = t.replace(")", "")                                          #Remove ')' resulting in t = 'r, g, b'
    t = tuple(map(int, t.split(', ')))                              #t = (r, g, b) (a tuple)

    return t

#Decodes a string into a renderable object
def objects_as_string_to_objects(string):
    objects = []                                                        #The list of objects
    objects_as_strings = string.split("|")                              #Converts the long string to a list of strings

    for string in objects_as_strings:                                   #For every string in the list of strings
        l = string.split("-")                                           #Separate the string into a list containing the attributes of the object
        t = l[3]                                                        #t = '(r, g, b)' (a string)
        t = string_to_tuple(t)                                          #t = (r, g, b) (a tuple)
        objects.append(game.GameObject(int(l[0]), int(l[1]), l[2], t, int(l[4])))  #Create an object 

    return objects

#The process that handles user input and sends it to the server
def user_interaction():
    while True:
        user_input = tdl.event.key_wait()               #The user key press
        byte_input = bytes(user_input.key, encoding)    #Converts the key press to sendable bytes
        s.send(byte_input)                              #Sends the bytes to the server

#Updates the screen
def update_graphics():
    while True:
        byte_message = s.recv(1024)                     #Receives the objects (as encoded bytes) from the server
        message = byte_message.decode(encoding)         #Decodes the bytes to a string
        objects = objects_as_string_to_objects(message) #Converts the string to objects
        graphics.render_all(objects)                    #Renders the objects and the map


s = global_variables.s                  #The socket
encoding = global_variables.encoding    #"UTF-8"
port = global_variables.port            #The port is 4444
s.connect((socket.gethostname(), port)) #Connect to the socket

print("CLIENT INITIATED")

graphics_thread = threading.Thread(target=update_graphics)  #The parallel thread that handles the updating of the screen
input_thread = threading.Thread(target=user_interaction)    #The parallel thread that handles user input

graphics_thread.start() #Start thread
input_thread.start()    #Start thread
