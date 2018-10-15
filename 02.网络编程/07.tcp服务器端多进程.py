from multiprocessing import Process
from socket import *


#接待客户端请求
def guest(new_socket, dest_addr):
	while True:
		recv_data = new_socket.recv(1024)
		if len(recv_data)>0:
			print('recv [{}]:{}'.format(str(dest_addr), recv_data))
		else:
			print('{}客户端已经关闭'.format(str(dest_addr)))
			break

	new_socket.close()

#1创建socket
ser_socket = socket(AF_INET, SOCK_STREAM)

#为了防止机器出现意外，导致端口没有释放
ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#2绑定本地IP和PORT
local_addr = ('', 2333)
ser_socket.bind(local_addr)

#3将socket变为监听(被动)套接字
ser_socket.listen(5)

def main():
	try:
		while True:
			print('====主进程，等待新客户的到来====')
			new_socket, dest_addr = ser_socket.accept()
			print('====主进程，，接下来创建一个新的进程负责数据处理{}===='.format(str(dest_addr)))
			client = Process(target = guest, args = (new_socket, dest_addr))
			client.start()
			#因为已经向子进程中copy了一份（引用），并且父进程中这个套接字也没有用处了
            #所以关闭
			new_socket.close()
	finally:
		ser_socket.close()
		print('程序结束')

if __name__ == '__main__':
	main()
