def insert_sort(aList):
    """插入算法"""
    # 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
    
    # 最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
    # 最坏时间复杂度：O(n2)
    # 稳定性：稳定

    n = len(aList)
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, n):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if aList[j] < aList[j-1]:
                aList[j], aList[j-1] = aList[j - 1], aList[j]

alist = [54,226,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)