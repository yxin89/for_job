def shell_sort(alist):
    """shell排序"""
    
    # 最优时间复杂度：根据步长序列的不同而不同
    # 最坏时间复杂度：O(n2)
    # 稳定想：不稳定

    n = len(alist)
    # 初始步长
    gap = n // 2

    while gap > 0:
         # 按步长进行插入排序
        for j in range(gap,n):
            i = j
            # 插入排序
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 得到新的步长
        gap //= 2

alist = [54,226,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)