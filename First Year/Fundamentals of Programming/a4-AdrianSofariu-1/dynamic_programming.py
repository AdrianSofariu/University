"""
Given the set of positive integers S, partition this set into two subsets S1 and S2
so that the difference between the sum of the elements in S1 and S2 is minimal.
For example, for set S = { 1, 2, 3, 4, 5 }, the two subsets could be S1 = { 1, 2, 4 }
and S2 = { 3, 5 }. Display at least one of the solutions.
"""
import math


def sum_array(arr: list) -> int:
    """
    Function to compute the sum of all elements in an array
    :param arr:
    :return: the sum of all elements in the array
    """
    s = 0
    for element in arr:
        s += element
    return s


def naive_solution(arr: list):
    """
    Implementation of the naive approach to solve the problem. To build
    the 2 subsets we look for the current maximum, and we add it to the
    subset with the smaller sum. Afterward we pop the maximum from the original set.
    We repeat this step until the original list is empty
    :param arr:
    :return:
    """
    arr1 = []
    arr2 = []

    while len(arr) != 0:
        maximum = -math.inf
        index_m = 0
        i = 0
        # find maximum
        for element in arr:
            if element > maximum:
                maximum = element
                index_m = i
            i += 1
        # decide where to append it
        if sum_array(arr1) < sum_array(arr2):
            arr1.append(maximum)
        else:
            arr2.append(maximum)
        # pop the maximum
        arr.pop(index_m)
    print(arr1, " ", arr2)


def dynamic_partition(arr: list):
    s = sum_array(arr)
    n = len(arr)
    sums_dict = {0: 0}

    # dp[i][j] = true if the sum j is possible using a subset of the first i elements
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]

    # initialize first column with True as s = 0 is possible with n elements
    for i in range(n + 1):
        dp[i][0] = True

    # initialize first row except [0][0] with False as no other sum is possible with 0 elements
    for i in range(1, s + 1):
        dp[0][i] = False

    # fill the table
    for i in range(1, n + 1):
        for j in range(1, s + 1):

            # if we exclude the i'th element
            dp[i][j] = dp[i - 1][j]

            # if we include the i'th element
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

            # add new entry in the hashmap of type sum: last element of sum
            if dp[i][j] and j not in sums_dict:
                sums_dict.update({j: arr[i - 1]})

    # for i in range(n + 1):
    #    print(dp[i])
    # print(sums_dict)

    diff = math.inf

    # find the biggest j , with j being the sum of S1
    # to minimize s - 2*j
    s1_sum = 0
    for j in range(s // 2, -1, -1):
        if dp[n][j] is True:
            s1_sum = j
            break

    # build the partitions
    s1 = []
    while s1_sum > 0:
        s1.append(sums_dict[s1_sum])
        s1_sum -= sums_dict[s1_sum]

    i = 0
    j = 0
    # search all elements that are in s1 and remove them to obtain s2
    while i < len(s1) and j < len(arr):
        if s1[i] == arr[j]:
            arr.pop(j)
            i += 1
            j = -1
        j += 1

    # print the partition
    print(s1)
    print(arr)
    print(sums_dict)
    for lst in dp:
        print(lst)


if __name__ == "__main__":
    # array = []
    # n = int(input("How long should the list be: "))
    # while n != 0:
    #     a = int(input("Add number to list: "))
    #     array.append(a)
    #     n -= 1
    array = [3, 1, 4, 2, 2, 1]
    # naive_solution(array)
    dynamic_partition(array)
