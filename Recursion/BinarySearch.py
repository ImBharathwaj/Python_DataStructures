class BinarySearch:
    @classmethod
    def BinarySearch(cls, arr, low, high, value):
        mid = int(low+(high-low)/2)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return cls.BinarySearch(arr, mid+1, high, value)
        elif arr[mid] < value:
            return cls.BinarySearch(arr, low, mid-1, value)

    @classmethod
    def main(cls):
        arr = [1,2,3,4,5,6,7,8,9]
        arrLen = len(arr)-1
        print(cls.BinarySearch(arr, 0, high=arrLen, value=3))

if __name__ == '__main__':
    bs = BinarySearch()
    bs.main()
