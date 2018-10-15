from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.sendto(b'fuck you', ('192.168.25.1', 8080))