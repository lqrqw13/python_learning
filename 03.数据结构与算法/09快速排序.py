'''快速排序'''
def fast_sort(alist, start, end):
    i = start
    j = end
    mid = alist[start]
    if start >= end:
        return alist

    while i < j:
        while i < j and alist[j] >= mid:
            j -= 1
        alist[i] = alist[j]

        while i < j and alist[i] < mid:
            i += 1
        alist[j] = alist[i]

    fast_sort(alist, start, i-1)
    fast_sort(alist, i+1, end)
    return alist

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('快速排序：', fast_sort(li, 0, len(li)-1))

