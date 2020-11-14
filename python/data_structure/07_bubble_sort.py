def double_sort(aList):
    """冒泡排序"""
    # 一次比较两个元素，如果他们的顺序错误就把他们交换过来
    # 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
    # 最坏时间复杂度：O(n2)
    # 稳定性：稳定

    n = len(aList)
    for i in range(n - 1,0,-1):
        for j in range(i):
            if aList[j] > aList[j+1]:
                aList[j],aList[j+1] = aList[j+1],aList[j]
        

a = [32,123,32,12,4,56,34,87]
double_sort(a)
print(a)
