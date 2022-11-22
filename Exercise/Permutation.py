class DS:
    @classmethod
    def permuation(cls, arr, i, length):
        if length == i:
            print(arr)
            return True
        j = i
        while j < length:
            cls.swap(arr, i, j)
            cls.permuation(arr, i + 1, length)
            cls.swap(arr, i, j)
            j += 1

    @classmethod
    def swap(cls, arr, x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp


if __name__ == "__main__":
    ds = DS
    arr = [None] * 5
    i = 0
    while i < 5:
        arr[i] = i
        i += 1
    print(ds.permuation(arr, 0, 5))