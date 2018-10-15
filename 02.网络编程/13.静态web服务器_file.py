from socket import *
from multiprocessing import Process
import re
#
# 根目录常量
HTML_ROOT = './html'

def func(client_socket, client_addr):
    '''处理客户端请求'''
    # 获取客户端请求数据
    # 此处因为是静态服务器，不需要多次通信，故不需要使用while循环,多次通信
    recvData = client_socket.recv(1024)
    request_data = recvData.splitlines()
    request_start_line = request_data[0].decode('utf-8')
    # GET /s?ie=UTF-8&wd=python%E8%BF%9B%E5%BA%A6%E6%9D%A1 HTTP/1.1
    request_path = re.match(r'\w+ (/[^ ]*)', request_start_line).group(1)
    # 默认主页
    if request_path == '/':
        file_path = './html/index.html'
    else:
        file_path =HTML_ROOT + request_path

    try:
        f = open(file_path, 'rb')
    except:
        response_start_line = 'HTTP/1.1 200 OK\r\n'
        response_headers = 'Server: My server\r\n'
        response_body = 'The file is missing'
    else:
        file_data = f.read()
        f.close()
        # 构造响应数据es
        response_start_line = 'HTTP/1.1 200 OK\r\n'
        response_headers = 'Server: My server\r\n'
        response_body = file_data.decode('utf-8')
    response = response_start_line + response_headers + '\r\n' + response_body
    # 会出现打印两次response的情况且最后一次会出现404 The file is missing。原因是favicon.ico是浏览器默认会载入的标签左上角icon，
    # 没有找到，所以显示404，无需关注.视情况需要可以加上该文件favicon.ico
    print('response_data:', response)
    # 两种写法response.encode('utf-8')或bytes(response, 'utf-8')
    client_socket.send(response.encode('utf-8'))
    client_socket.close()


ser_socket = socket(AF_INET, SOCK_STREAM)



def main():
    while True:
        client_socket, client_addr = ser_socket.accept()
        p = Process(target=func, args=(client_socket, client_addr))#格式注意参数等号两边不空格
        p.start()
        client_socket.close()
    ser_socket.close()

ser_socket.bind(('', 2333))

ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ser_socket.listen(5)

if __name__ == '__main__':
    main()
