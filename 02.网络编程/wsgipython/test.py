class A(object):
    def __init__ (self):
        pass

    def __call__(self, func):
        status = '200'
        func(status)

class B(object):
    def __init__(self, a):
        self.a = a

    def func(self, status):
        response_header = status + ' OK'
        self.response_header = response_header

    def start(self):
        response_body = self.a(self.func)
        response = self.response_header +'\r\n' + response_body
        return response

a = A()
b = B(a)
c = b.start()
print(c)
