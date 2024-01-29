# Iterative Method
def binarySearch(arr, lb, ub, key):

    while lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            lb = mid+1
        elif key < arr[mid]:
            ub = mid-1
    return -1


if __name__ == "__main__":
    arr = [2, 4, 5, 9, 11, 23, 34, 55]
    lb = 0
    ub = len(arr) - 1
    print(binarySearch(arr, lb, ub, 11))
    print(binarySearch(arr, lb, ub, 22))
