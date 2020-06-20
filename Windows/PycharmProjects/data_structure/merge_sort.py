# coding:utf-8


def merge_sort(a_list):
    n = len(a_list)
    if n <= 1:
        return a_list

    mid = n//2

    left = merge_sort(a_list[:mid])
    right = merge_sort(a_list[mid:])

    # 合并两个子列需要两个指针
    result = []
    left_p = 0
    right_p = 0
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1

    result += left[left_p:]
    result += right[right_p:]
    return result


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 34, 1, 89, 144, 21, 13, 55]
    print(test_list)
    print(merge_sort(test_list))