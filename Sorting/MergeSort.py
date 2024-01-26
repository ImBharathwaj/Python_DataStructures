# Time complexity: O(nlog n)
def mergeSort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        leftArr = arr[:r]
        rightArr = arr[r:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        # merge(arr, lb, mid, ub)

        # To sort the sublist
        i = j = k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        # If the value of i become smaller than length of leftArr
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        # If the value of j become smaller than length of rightArr
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [15, 5, 24, 8, 1, 3, 16, 10, 20]
    print(arr)
    mergeSort(arr)
    print(arr)
