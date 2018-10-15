from socket import * 

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('',2333))
ret = udp_socket.recvfrom(1024)

print(ret)
udp_socket.sendto(b'fuck you very much',('192.168.123.227',2333))
