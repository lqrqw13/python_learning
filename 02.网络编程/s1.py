import socket
from threading import Thread


def handle_client(socket_client, info):
    """处理客户端请求"""
    # 获取客户端请求数据
    global clients
    request_data = socket_client.recv(1024)
    print("request data:", request_data)
    clients.append((socket_client, info))




if __name__ == "__main__":
    clients = []
    socket_servers = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建大套接字
    socket_servers.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 立即释放端口
    socket_servers.bind(('', 15926))
    # 绑定端口
    socket_servers.listen(5)
    # 转为被动接收
    while True:
        socket_client, info = socket_servers.accept()
        # 接收链接,产生小套接字
        print(info, '链接成功了')
        handle_client_thread = Thread(target=handle_client, args=(socket_client, info))
        handle_client_thread.start()
        handle_client_thread.join()
        client1, info1 = clients[0]
        client1.send(b'sssss')
        # 关闭客户端连接
        #client1.close()

    socket_servers.close()





# info_old = info
# print(socket_client)
# print(info)
# socket_client.send('哈哈'.encode('utf-8'))

# socket_client, info = socket_servers.accept()
# # 接收链接,产生小套接字
# print(info, '链接成功了')
# print(socket_client)
# print(info)
# socket_client.send('嘿嘿'.encode('utf-8'))
# socket_client.send('吼吼'.encode('utf-8'))
# socket_client.close()


# socket_servers.close()