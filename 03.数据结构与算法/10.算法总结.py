# encoding=utf-8
# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
# from time import time
#
# start = time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         c=1000-a-b
#         if a + b + c == 1000 and a**2 + b**2 == c**2:
#             print(a, b ,c)
# end = time()
# print(f'time: {end - start:.2f}秒')

'''冒泡排序'''
# 从0下标开始，i和i+1比较，交换位置，把最大数排到最后
def bubble_sort(alist):
    n = len(alist)
    # 内循环走一次找到一个最大数，找到n-1个最大数即可，也就是循环执行n-1次
    for j in range(0, n-1):
        # range后面的一个位置是动态变化的，所以是n-1-j
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist



'''选择排序'''
# 从0下标开始，设min_index = 0, i和i+1, i+2, ...n-1比较，记录最小数下标,然后交换位置
def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index= j
        for i in range(j+1,n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist



'''插入排序'''
# 首先在未排序序列中找到最小元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中取一个和排序序列比较
# 然后放到已排序序列相应位置。以此类推，直到所有元素均排序完毕。
def insert_sort(alist):
    n = len(alist)
    for j in range(1,n):
        for i in range(j, 0, -1):
            if alist[i-1] > alist[i]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
            else:
                break
    return alist



'''希尔排序'''
#

'''快速排序'''
def fast_sort(alist, start, end):
    i = start
    j = end
    mid = alist[start]
    # 递归退出条件
    if start >= end:
        # 另外列表只有一个元素时，返回列表本身，因为不需要排序
        return alist
    while i < j:
        # 1如果mid值从start取，则必须J指针先跑，这样碰到比mid小的值，就可以赋给i, 否则i指针一开始就是mid值，
        # 然后产生死循环。alist[j]>=mid不写等号会死循环，如果最后个数等于mid,则会把mid的赋给i，然后互相给
        # 对方赋值，进入死循环
        while i < j and alist[j]>=mid:
                j -=1
        alist[i]= alist[j]
        while i < j and alist[i] < mid:
                i += 1
        alist[j] = alist[i]


    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[i] = mid

    fast_sort(alist, start, i-1)
    fast_sort(alist, i+1, end)
    return alist


'''归并排序'''
def merge_sort(alist):
    n = len(alist)
    if n <=1:
        return alist
    mid_index = n//2
    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid_index])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid_index:])
    left_pointer, right_pointer = 0, 0
    # 保存返回新表的元素
    result = []
    while left_pointer<len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer]< right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer +=1
        else:
            result.append(right_li[right_pointer])
            right_pointer +=1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

'''二分查找法递归法'''
def binary_search_1(alist, item):
    n = len(alist)
    if n <= 0:
        return False
    mid = n//2
    if item == alist[mid]:
        return True
    elif item> alist[mid]:
        return binary_search_1(alist[mid+1:], item)
    else:
        return binary_search_1(alist[:mid], item)

'''二分查找法循环法'''
def binary_search_2(alist, item):
    n = len(alist)
    start = 0
    end = n-1
    while start <=end:
        mid = (start+end)//2
        if item == alist[mid]:
            return True
        elif item > alist[mid]:
            start = mid+1
        else:
            end = mid -1
    return False


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('冒泡排序：' ,bubble_sort(li))
    print('选择排序：', select_sort(li))
    print('插入排序：', insert_sort(li))
    print('快速排序：', fast_sort(li, 0 , len(li)-1))
    print('归并排序：', merge_sort(li))
    alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print('二分查找法递归法：', binary_search_1(alist, 20))
    print('二分查找法循环法：', binary_search_2(alist, 30))

