import math


def metaBinarySearch(arr, key):
    n = len(arr)
    math_log = int(math.log2(n - 1)) + 1
    pos = 0

    for i in range(math_log - 1, -1, -1):
        if arr[pos] == key:
            return pos
        new_pos = pos | (1 << i)
        if (new_pos < n) and (arr[new_pos] <= key):
            pos = new_pos
    return pos if (arr[pos] == key) else -1


if __name__ == "__main__":
    arr = [2, 3, 4, 6, 7]
    key = 3
    print(metaBinarySearch(arr, key))
