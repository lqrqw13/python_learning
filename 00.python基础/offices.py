import random

offices = [[],[],[]]
teachers = ['a','b','c','d','e','f','g','h']
for teacher in teachers:
    nums = random.randint(0,2)
    offices[nums].append(teacher)

i = 1
for office in offices:
    print('office{} has{} teachers, names are {}'.format(i,len(office),office))
    i +=1
