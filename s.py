#!/bin/python3

import socket


HOST ='127.0.0.1'
PORT = 7777

#Small program to listen with netcat

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #The Variable s has a value socket.socket(socket.AF INET***ip>
s.connect ((HOST,PORT))

