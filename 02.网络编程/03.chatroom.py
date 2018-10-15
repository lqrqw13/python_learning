from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('',2333))
while True:
    recv = udp_socket.recvfrom(1024)
    print(recv)
