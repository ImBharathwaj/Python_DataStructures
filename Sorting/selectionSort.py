def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i

        # Range of inner loop should be starts after
        # sorted part of array
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j

        # # Swapping
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp


def printArr(arr):
    for a in arr:
        print(a, end=" ")
    print()


if __name__ == "__main__":
    arr = [7, 4, 10, 8, 3, 1]
    printArr(arr)
    selectionSort(arr)
    printArr(arr)
