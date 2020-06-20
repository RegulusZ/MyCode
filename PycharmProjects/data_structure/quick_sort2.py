# coding:utf-8


def quick_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    mid_value = a_list[0]
    left = []
    right = []
    a_list.remove(mid_value)
    for i in a_list:
        if i >= mid_value:
            right.append(i)
        else:
            left.append(i)

    a = quick_sort(left) + [mid_value] + quick_sort(right)
    return a


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 34, 1, 89, 144, 21, 13, 55]
    print(test_list)
    print(quick_sort(test_list))