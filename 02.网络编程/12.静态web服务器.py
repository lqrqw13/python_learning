from socket import *
from multiprocessing import Process


def func(client_socket, client_addr):
    '''处理客户端请求'''
    # 获取客户端请求数据
    # 此处因为是静态服务器，不需要多次通信，故不需要使用while循环,多次通信
    recvData = client_socket.recv(1024)
    print('recvData:', recvData)
    # 构造响应数据es
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: My server\r\n'
    response_body = 'Hello itcast'
    response = response_start_line + response_headers + '\r\n' + response_body
    print('response_data:', response)
    # 两种写法response.encode('utf-8')或bytes(response, 'utf-8')
    client_socket.send(response.encode('utf-8'))


    client_socket.close()

if __name__ == '__main__':
    ser_socket = socket(AF_INET, SOCK_STREAM)

    ser_socket.bind(('', 2333))

    ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    ser_socket.listen(5)

    while True:
        client_socket, client_addr = ser_socket.accept()
        p = Process(target=func, args=(client_socket, client_addr))#格式注意参数等号两边不空格
        p.start()
        client_socket.close()
    ser_socket.close()
