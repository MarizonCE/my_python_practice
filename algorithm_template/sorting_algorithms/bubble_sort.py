def bubble_sort(arr: list) -> list:
    """
    Bubble Sort Algorithm
    :param arr:待排序的可比较元素列表
    :return:从小到大排序后的新列表

    算法原理:
    - 冒泡排序是一种基于交换的排序方法
    - 每次遍历将当前未排序部分中最大的元素“冒泡”到末尾
    - 当一轮遍历中未发生任何交换，说明数组已排序，可提前终止
    """
    n = len(arr)
    # 创建 arr 的副本以避免修改原始记录
    sorted_arr = arr.copy()

    for i in range(n - 1):
        # 添加标志位用于优化，若本轮未交换，提前终止
        swapped = False
        for j in range(n - 1 - i):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # 交换相邻元素
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break  # 已排序，无需继续

    return sorted_arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubble_sort(data)
    print("原始数据:", data)
    print("排序后的数据:", sorted_data)