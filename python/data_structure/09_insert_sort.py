def insert_sort(aList):
    """插入算法"""
    n = len(aList)
    for i in range(1, n):
        for j in range(i,0,-1):
            if aList[j] < aList[j-1]:
                aList[j], aList[j-1] = aList[j - 1], aList[j]

alist = [54,226,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)