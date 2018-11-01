import time

def index():
    return "这是主页"

def login():
    return'welcome to joyland'

def show_ctime():
    return time.ctime()


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']

    if file_name == '/index.py':
        return index()
    elif file_name =='/login.py':
        return login()
    elif file_name =='/show_ctime.py':
        return show_ctime()
    else:
        return 'Hello World! 我爱你中国....'