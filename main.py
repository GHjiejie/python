# 声明变量
nums = [3, 5, 2, 7, 4]
name = str("jiejie")
print("Hello, " + name)


def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


sorted_nums = bubble_sort(nums)
print("Sorted array is:", sorted_nums)
