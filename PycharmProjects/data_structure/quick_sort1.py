# coding:utf-8


def quick_sort(a_list, start, end):
    if start >= end:
        return
    low = start
    high = end
    mid_value = a_list[start]

    while low < high:
        while low < high and a_list[high] >= mid_value:
            high -= 1
        a_list[low] = a_list[high]
        while low < high and a_list[low] < mid_value:
            low += 1
        a_list[high] = a_list[low]

    a_list[low] = mid_value

    quick_sort(a_list, 0, low-1)
    quick_sort(a_list, low+1, end)


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 1, 34, 89, 144, 21, 13, 55]
    print(test_list)
    quick_sort(test_list, 0, len(test_list)-1)
    print(test_list)