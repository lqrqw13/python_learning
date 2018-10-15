from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('192.168.123.227', 2333))

client_socket.send(b'fuck you')

client_socket.close()