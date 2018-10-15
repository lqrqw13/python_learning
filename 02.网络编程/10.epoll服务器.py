from socket import *
from select import *


ser_socket = socket(AF_INET, SOCK_STREAM)

ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ser_socket.bind(('', 2333))

ser_socket.listen(5)

epoll = epoll()

epoll.register(ser_socket.fileno(), EPOLLIN|EPOLLET)


clients = {}
addresses = {}

while True:
    epoll_list = epoll.poll()
    for fd,events in epoll_list:
        if fd == s.fileno():
            client,addr=s.accept()
            print('有新的客户端到来%s'%str(addr))
            # 将 conn 和 addr 信息分别保存起来
            clients[client.fileno()] = client
            addresses[client.fileno()] = addr
            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

        elif events == select.EPOLLIN:
            # 从激活 fd 上接收
            recvData = clients[fd].recv(1024)

            if len(recvData)>0:
                print('recv:%s'%recvData)
            else:
                # 从 epoll 中移除该 连接 fd
                epoll.unregister(fd)

                # server 侧主动关闭该 连接 fd
                clients[fd].close()

                print("%s---offline---"%str(addresses[fd]))
