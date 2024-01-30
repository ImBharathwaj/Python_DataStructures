import math


def jumpSearch(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < key:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == key:
        return prev
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 6
    print(jumpSearch(arr, key))
