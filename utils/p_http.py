#!/usr/bin/env python3
# coding=utf-8

import socket

host = ''
port = 2000

s = socket.socket()
s.bind((host, port))

while True:
    s.listen(5)
    connection, address = s.accept()

    request = connection.recv(1024)

    print(address)

    print('ip and request,{}\n{}'.format(address,request.decode('utf-8')))

    response = b'<h1>hello world!</h1>'

    connection.sendall(response)
    connection.close()