def repeat(arr):
    size = len(arr)
    i = 0
    arr.sort()
    print('Repeating elements are :: ')
    while i < size:
        if arr[i] == arr[i-1]:
            print(arr[i])
        i += 1

if __name__ == '__main__':
    repeat([1,2,3,2,4,4,4,1,2,5,6,4,5,6])
