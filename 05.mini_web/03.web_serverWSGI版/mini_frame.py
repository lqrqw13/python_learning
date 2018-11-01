import time


URL_FUNC_DICT = dict()


def route(url):
    def decorate(func):
        URL_FUNC_DICT[url] = func
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    # 忘记写这句TypeError: 'NoneType' object is not callable
    return decorate


@route('/login.py')
def login():
    return 'This is the login page'


@route('/show_time.py')
def show_time():
    return time.ctime()


def application(env, start_response):
    file_name = env['PATH_INFO']
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf-8')])
    # if file_name == "/login.py":
    #     return login()
    # elif file_name == "/show_time.py":
    #     return show_time()
    # else:
    #     return 'Hello World! 我爱你中国....'
    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return 'Error {}'.format(ret)