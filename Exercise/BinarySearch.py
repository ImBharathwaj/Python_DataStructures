class DS:
    @classmethod
    def BinarySearchRecursive(cls, arr, low, high, value):
        mid = int(low + (high - low) / 2)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return cls.BinarySearchRecursive(arr, mid + 1, high, value)
        else:
            return cls.BinarySearchRecursive(arr, low, mid - 1, value)

    @classmethod
    def main(cls):
        arr = list(range(10))
        high = len(arr)
        low = 0
        print(cls.BinarySearchRecursive(arr,low, high, 6))
        print(cls.BinarySearchRecursive(arr,low, high, 16))
if __name__ == "__main__":
    ds = DS
    ds.main()