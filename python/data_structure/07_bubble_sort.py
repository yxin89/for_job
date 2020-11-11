def double_sort(aList):
    """冒泡排序"""
    n = len(aList)
    for i in range(n - 1,0,-1):
        for j in range(i):
            if aList[j] > aList[j+1]:
                aList[j],aList[j+1] = aList[j+1],aList[j]
        

a = [32,123,32,12,4,56,34,87]
double_sort(a)
print(a)
