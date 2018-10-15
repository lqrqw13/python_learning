from socket import *

def msg_send():
    client_socket.connect(('192.168.123.227', 15926)) #使用线程会报错，占用端口？OSError: [WinError 10022] 提供了一个无效的参数。

    client_socket.send(b'hello')

    recv_data = client_socket.recv(1024)
    print(f'{recv_data}')
    client_socket.close()


if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)
    msg_send()


# client_socket = socket(AF_INET, SOCK_STREAM)
# client_socket.connect(('192.168.123.231', 2333))
# client_socket.send(b'fuck you')
# client_socket.close()
