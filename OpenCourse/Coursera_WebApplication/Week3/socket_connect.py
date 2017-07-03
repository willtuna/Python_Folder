# coding=UTF-8
#!/usr/env python2.7
import socket



MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MySocket.connect(("data.pr4e.org", 80))

MySocket.send("GET http://data.pre4e.org/code/romeo.txt HTTP/2.0\r\n\r\n")

while True:
    data = MySocket.recv(512)
    if not data:
        break
    print data


MySocket.close() 
