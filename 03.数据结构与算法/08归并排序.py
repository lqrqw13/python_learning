'''归并排序'''
def merge_sort(alist):
    n = len(alist)
    if n <=1:
        return alist
    mid_index = n//2
    left_lst= merge_sort(alist[:mid_index])
    right_lst = merge_sort(alist[mid_index:])
    result = []
    i, j = 0, 0

    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] < right_lst[j]:
            result.append(left_lst[i])
            i +=1
        else:
            result.append(right_lst[j])
            j +=1
    result += left_lst[i:]
    result += right_lst[j:]
    return result
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('归并排序：', merge_sort(li))
