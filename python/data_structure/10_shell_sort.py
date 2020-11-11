def shell_sort(alist):
    """shell排序"""
    n = len(alist)
    gap = n // 2

    while gap > 0:
        for j in range(gap,n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

alist = [54,226,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)