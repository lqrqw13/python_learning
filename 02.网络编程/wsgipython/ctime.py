from time import ctime

def application(env, start_response):
    #env = {}
    status = "200 OK"
    # "Content-Type","text/plain" 妈的，写成单引号会报错。。。。
    # local variable 'response' referenced before assignment
    headers = [("Content-Type","text/plain")]
    start_response(status, headers)
    return ctime()
