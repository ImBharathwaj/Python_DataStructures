def partition(arr, lb, ub):
    # Pivot element
    pivot = arr[ub]

    # Starting element
    i = lb - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(lb, ub):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[ub]) = (arr[ub], arr[i + 1])
    return i + 1


def quickSort(arr, lb, ub):
    if lb < ub:
        loc = partition(arr, lb, ub)
        quickSort(arr, lb, loc - 1)
        quickSort(arr, loc + 1, ub)


def printArr(arr):
    for i in arr:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
    lb = 0
    ub = len(arr) - 1
    printArr(arr)
    quickSort(arr, lb, ub)
    printArr(arr)
