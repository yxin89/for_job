# 确定一个元素，通过前后两个游标同时向中间移动找到其位置

def quick_sort(alist, start, end):
    """快速排序"""

    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(n2)
    # 稳定性：不稳定

    # 推出条件
    if start > end:
        return

    mid_value = alist[start]
    low = start 
    high = end

    while low < high:
        # high游标左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        # low游标右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid_value

     # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist,low+1,end)
    

alist = [54,226,93,17,77,31,44,55,20]
quick_sort(alist,0, len(alist)-1)
print(alist)