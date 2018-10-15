from threading import Thread 
from socket import *

#1接收功能,需要先绑端口
def recv():
    while True:
        ret = udp_socket.recvfrom(1024) #一开始recvfrom 写成recv，结果提示AttributeError: 'int' object has no attribute 'decode'
        print(ret[0].decode('gb2312') + ' sent from ' +str(ret[1]))#str(ret[1])而不是ret[1]
        

#2发送功能
def sendto():
    while True:
        
        send_data = input('<<')
        udp_socket.sendto(send_data.encode("gb2312"),(dest_ip, dest_port))
        #要加上.encode("gb2312")，否则提示Socket TypeError: a bytes-like object is required, not 'str' 

#定义空的全局变量，然后在main函数中修改，以达到recv和sendto可以调用的目的
udp_socket = None
dest_port = 0
dest_ip = ''
#3主函数开两线程
def main():
    global udp_socket
    global dest_port
    global dest_ip
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 2333))
    dest_ip = input('请输入对方IP:')
    dest_port = int(input('请输入对方端口：'))
    tr = Thread(target = recv)
    ts = Thread(target = sendto)
    tr.start()
    ts.start()
    tr.join()
    ts.join()

if __name__ == '__main__':
    main()
