#内建函数
#map函数
a = [1,2,3]
b = [2,3,4]
c = map(lambda x, y: x+y,a, b)
for temp in c:
    print(temp)



#filter函数
d = filter(lambda x: x>=170,[x for x in range(180)] )
for temp in d:
    print(temp)


#reduce函数
