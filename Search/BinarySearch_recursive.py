# Iterative Method
def binarySearch(arr, lb, ub, key):
    if ub >= lb:
        mid = (lb + ub) // 2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            return binarySearch(arr, mid+1, ub, key)
        elif key < arr[mid]:
            return binarySearch(arr, lb, mid-1, key)
    return -1


if __name__ == "__main__":
    arr = [2, 4, 5, 9, 11, 23, 34, 55]
    lb = 0
    ub = len(arr) - 1
    print(binarySearch(arr, lb, ub, 11))
    print(binarySearch(arr, lb, ub, 22))
