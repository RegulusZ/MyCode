# coding:utf-8
# [1,1,2,3,5,8,13,21,34,55,89,144]
# [2,1,3,5,8,34,1,89,144,21,13,55]


def shell_sort(a_list):
    n = len(a_list)
    step = 4
    while step >= 1:
        for j in range(n-step):
            for i in range(j+step, 0, -step):
                if a_list[i] < a_list[i-step]:
                    a_list[i], a_list[i-step] = a_list[i-step], a_list[i]
                else:
                    break
        step //= 2


if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 8, 34, 1, 89, 144, 21, 13, 55]
    print(test_list)
    shell_sort(test_list)
    print(test_list)