def select_sort(aList):
    """选择排序--不稳定"""
    # 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    
    # 最优时间复杂度：O(n2)
    # 最坏时间复杂度：O(n2)
    # 稳定性：不稳定（考虑升序每次选择最大的情况）


    n = len(aList)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1,n):
            if aList[i] > aList[j]:
                aList[i], aList[j] = aList[j], aList[i]


alist = [54,226,93,17,77,31,44,55,20]
select_sort(alist)
print(alist)