def merge_sort(alist):
    """归并排序"""
    
    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(nlogn)
    # 稳定性：稳定

    n = len(alist)
    if n <= 1:
        return alist

    num = n // 2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])

    print('*'*50)
    print(left)
    print(right)

    return merge(left, right)

def merge(left, right):

    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    #left与right的下标指针
    r, l = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])

    return result

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
sorted_alist = merge_sort(alist)
print(sorted_alist)