def ternarySearch(arr, key, lb, ub):
    if ub >= lb:
        mid1 = lb + (ub - lb) // 3
        mid2 = ub - (ub - lb) // 3

        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2

        if key < arr[mid1]:
            return ternarySearch(arr, key, lb, mid1 - 1)
        elif key > arr[mid2]:
            return ternarySearch(arr, key, mid2 + 1, ub)
        else:
            return ternarySearch(arr, key, mid1 + 1, mid2 - 1)
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 6
    lb = 0
    ub = len(arr)
    print(ternarySearch(arr, key, lb, ub))
