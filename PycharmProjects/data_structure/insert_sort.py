# coding:utf-8
# [1,1,2,3,5,8,13,21,34,55,89,144]
# [2,1,3,5,8,34,1,89,144,21,13,55]


def insert_sort(a_list):
    n = len(a_list)
    for i in range(n-1):
        for j in range(i+1, 0, -1):
            if a_list[j] < a_list[j-1]:
                a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            else:
                break


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 34, 1, 89, 144, 21, 13, 55]
    print(test_list)
    insert_sort(test_list)
    print(test_list)