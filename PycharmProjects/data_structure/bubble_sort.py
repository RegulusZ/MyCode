# coding:utf-8
# [1,1,2,3,5,8,13,21,34,55,89,144]
# [2,1,3,5,8,34,1,89,144,21,13,55]


def bubble_sort(a_list):
    n = len(a_list)

    for i in range(n-1):
        is_sorted = 0
        for j in range(n-1-i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                is_sorted += 1
        if is_sorted == 0:
            return


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 34, 1, 89, 144, 21, 13, 55]
    print(test_list)
    bubble_sort(test_list)
    print(test_list)