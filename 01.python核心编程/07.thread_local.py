from threading import Thread, local, current_thread

#local()当全局变量使，线程中数据互不影响
local_school = local()

def process_student():
    std = local_school.student

    print('Hello,{} (in{})'.format(std, current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = Thread(target = process_thread, args = ('dongGe',), name = 'T1')
t2 = Thread(target = process_thread, args = ('老王',), name = 'T2')
t1.start()
t2.start()
# t1.join()
# t2.join()