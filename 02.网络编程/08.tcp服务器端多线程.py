from socket import *
from threading import Thread


def guest(client_socket, client_addr):
	while True:
		recv_data = client_socket.recv(1024)
		if len(recv_data)>0:
			print('{} sent from {}'.format(recv_data, str(client_addr)))
		else:
			print('客户端已经关闭')
			break
	client_socket.close()

#1创建套接字
ser_socket = socket(AF_INET, SOCK_STREAM)

#2程序意外退出，需要释放端口 
ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


#3绑定端口
local_addr = ('', 2333)
ser_socket.bind(local_addr)

#4创建listen套接字，转为被动接收
ser_socket.listen(5)

def main():
	try:
		while True:
			#5创建客户端套接字
			client_socket, client_addr = ser_socket.accept()
			print('客户端{}已连接'.format(client_addr))
			#6创建多线程
			client = Thread(target = guest, args=(client_socket, client_addr))
			client.start()
	finally:
		ser_socket.close()
		print('程序结束')
	
if __name__ == '__main__':
	main()

