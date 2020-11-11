def select_sort(aList):
    """选择排序--不稳定"""

    n = len(aList)
    for i in range(n-1):
        for j in range(i+1,n):
            if aList[i] > aList[j]:
                aList[i], aList[j] = aList[j], aList[i]


alist = [54,226,93,17,77,31,44,55,20]
select_sort(alist)
print(alist)