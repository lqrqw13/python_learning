from socket import *
from multiprocessing import Process
import re
import mini_frame


class WSGI_server(object):
    def __init__(self):
        # 1. 创建套接字
        self.ser_socket = socket(AF_INET, SOCK_STREAM)
        self.ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 2. 绑定
        self.ser_socket.bind(('', 2333))
        # 3. 变为监听套接字
        self.ser_socket.listen(128)

    def ser_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求
        # GET / HTTP/1.1
        # GET /match/teamList?match_id=12 HTTP/1.1
        request = new_socket.recv(1024).decode("utf-8")
        request_lines = request.splitlines()
        # IndexError: list index out of range 
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'
        if file_name.endswith('.py'):
            env = dict()
            env['PATH_INFO'] = file_name
            body = mini_frame.application(env, self.set_response_header)
            header = "HTTP/1.1 %s\r\n" % self.status

            for i, j in self.headers:
                header += "%s:%s\r\n" % (i, j)

            header += "\r\n"

            response = header + body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))
        else:
            try:
                with open('./html' + file_name, "r") as f:
                    body = f.read()
                    # 2.1 准备发送给浏览器的数据---header
                header = "HTTP/1.1 200 OK\r\n"
            except:
                header = "HTTP/1.1 404 NOT FOUND\r\n"
                body = "------file not found-----"
            finally:
                # 将response header发送给浏览器
                response = header +"\r\n"+ body
                new_socket.send(response.encode("utf-8"))

        # 发送response给浏览器
        new_socket.close()

        
    def set_response_header(self, status, headers):
        self.status = status
        self.headers = headers
        self.headers += [("server", "mini_web v8.8")]
        




    def run(self):
        while True:
            # 4. 等待新客户端的链接
            new_socket, info = self.ser_socket.accept()
            # 5. 为这个客户端服务
            p = Process(target= self.ser_client, args=(new_socket,))
            p.start()
            # 关闭原客户端套接字
            new_socket.close()

        # 关闭监听套接字
        self.ser_socket.close()



def main():
    wsgi_server = WSGI_server()
    wsgi_server.run()

if __name__=='__main__':
    main()