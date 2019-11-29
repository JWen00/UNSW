import sys
import os
from os import path
from socket import *

if len(sys.argv) < 2:
    print("Usage: python WebServer.py <port>")
    sys.exit()

# Create a connection when contacted by a client
serverPort = int(sys.argv[1])
serverName = "localhost"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("Socket is listening on 127.0.0.1:" + str(serverPort))

# Receive HTTP request from this connection (Only GET requests)
while 1:
    connectionSocket, addr = serverSocket.accept()

    
    GETRequest = connectionSocket.recv(1024)
    parser = GETRequest.split(" ")
    path = parser[1]
    path = path[1:]
    fileData = None

    if not os.path.exists(path):
        responseHeader = "HTTP/1.1 404 File Not Found\r\n"
        responseServer = "Server: " + serverName + "\r\n"
        responseConnection = "Connection: keep-alive\r\n"

        # responseConnection = "Connection: close\r\n" 
        response = responseHeader + responseServer + responseConnection + "\r\n" 
         

    else:
        fileSize = os.path.getsize(path) 

        with open(path, "r") as f:
            fileData = f.read()
            print(fileData)
        responseHeader = "HTTP/1.1 200 OK\r\n"
        responseServer = "Server: " + serverName + "\r\n"
        responseLength = "Content-Length: " + str(fileSize) + "\r\n" 
        responseConnection = "Connection: keep-alive\r\n"
        response = responseHeader + responseServer + responseLength + responseConnection + "\n" + fileData + "\r\n" 
        
    # response = response.encode("utf-8")
    print(response)
    connectionSocket.send(response)
