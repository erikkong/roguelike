import socket               #To handle the transmission of data
import global_variables     #Variables such as port number and the socket

import game                 #The mechanics of the game
import threading            #To run things in parallel

#Converts the list of objects to sendable bytes
def objects_to_bytes(objects):
    objects_as_strings = map(str, objects)              #Convert every object to a string describing the object
    string_of_objects = "|".join(objects_as_strings)    #Convert the list of strings to a long string
    byte_objects = bytes(string_of_objects, encoding)   #Convert the string to sendable bytes
    return byte_objects                                 #Return the sendably bytes

#Given an input sends the new object states to all of the clients
def process_input(user_input, player):
    if user_input not in allowed_inputs:
        return
    
    game.handle_key(user_input, player)             #Converts the input to an action in the game
    objects_as_bytes = objects_to_bytes(objects)    #Converts the states of the objects to sendable bytes
    for clientsocket in clientsockets:              #For every client
        clientsocket.send(objects_as_bytes)         #Send the new state of the objects

#The function handles all inputs from a client
def client_input_loop(clientsocket, player):
    while True:                                     #Repeat forever
        byte_input = clientsocket.recv(1024)        #Receive the encoded message
        user_input = byte_input.decode(encoding)    #Decode the encoded message
        process_input(user_input, player)           #Process the message
        



encoding = global_variables.encoding    #"UTF-8"
port = global_variables.port            #The port is 4444

s = global_variables.s                  #The socket to use
s.bind((socket.gethostname(), port))    #Binds the socket to the port                
s.listen()                              #Listen to the data coming in to the port
print("SERVER INITIATED")

clientsockets = []                      #The list of connected clients

allowed_inputs = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SPACE']

while True:
    clientsocket, adress = s.accept()           #Accept connection
    clientsockets.append(clientsocket)          #Add the client socket to the list of client sockets
    connected_clients = len(clientsockets)      #The number of connected clients
    
    print("Connection from", adress)            
    objects = game.objects                      #The current state of the objects
    
    byte_objects = objects_to_bytes(objects)    #Convert the current state of the objects to UTF-8 bytes
    clientsocket.send(byte_objects)             #Send the current state of objects (as bytes) to the just connected client

    if connected_clients <= 2:                                                          #All clients after the first 2 may only watch
        player = objects[connected_clients - 1]                                         #objects[0] or objects[1]
        t = threading.Thread(target=client_input_loop, args=[clientsocket, player])     #Handle client inputs in parallel
        t.start()                                                                       #Start the parallel process











