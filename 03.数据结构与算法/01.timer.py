
		li.append(i)


def test2():
	global li
	for i in range(10000):
		li += [i]

def test3():
	global li
	li = [i for i in range(10000)]

def test4():
	global li
	li = list(range(10000))
# Timer第一个参数是要执行的函数， 第二个是导入的方法
timer1 = Timer('test1()', 'from __main__ import test1')
# timeit内的参数为执行多少次，返回值是执行时间
print("+:", timer1.timeit(1000))
timer2 = Timer('test2()', 'from __main__ import test2')
print("+:", timer2.timeit(1000))
timer3 = Timer('test3()', 'from __main__ import test3')
print("+:", timer3.timeit(1000))
timer4 = Timer('test4()', 'from __main__ import test4')
print("+:", timer4.timeit(1000))
