def linearSearch(arr, key):
    n = len(arr)
    flag = -1
    for i in range(n):
        # print(i)
        if arr[i] == key:
            flag = i
    print(flag)


if __name__ == "__main__":
    arr = [43, 1, 52, 53, 5, 2, 44, 94]
    print(arr)
    linearSearch(arr, 32)
    linearSearch(arr, 1)
