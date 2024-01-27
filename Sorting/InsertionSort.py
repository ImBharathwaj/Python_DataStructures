def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        # index of sorted array
        j = i - 1

        # checks both the conditions
        # whether last element of sorted list and current element of unsorted list
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            # moving sorted array index in backward by decrementing
            j -= 1

        arr[j + 1] = temp


def printArr(arr):
    for a in arr:
        print(a, end=" ")
    print()


if __name__ == "__main__":
    arr = [5, 4, 10, 1, 6, 2]
    printArr(arr)
    insertionSort(arr)
    printArr(arr)
