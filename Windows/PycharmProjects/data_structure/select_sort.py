# coding:utf-8
# [1,1,2,3,5,8,13,21,34,55,89,144]
# [2,1,3,5,8,34,1,89,144,21,13,55]


def select_sort(a_list):
    n = len(a_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if a_list[min_index] > a_list[j]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 34, 1, 89, 144, 21, 13, 55]
    print(test_list)
    select_sort(test_list)
    print(test_list)