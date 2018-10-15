#协程的好处，可以自主控制并发的顺序
from greenlet import greenlet
from time import sleep

def A():
	while True:
		print('===A===')
		gr2.switch()
		sleep(0.5)

def B():
	while True:
		print('===B===')
		gr1.switch()
		sleep(0.5)

gr1 = greenlet(A)
gr2 = greenlet(B)

gr1.switch()
