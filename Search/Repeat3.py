def Repeat(arr):
    size = len(arr)
    hs = set()
    i = 0
    while i < size:
        if arr[i] in hs:
            print(arr[i])
        else:
            hs.add(arr[i])
        i+=1
    print(hs)
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    Repeat(arr)
