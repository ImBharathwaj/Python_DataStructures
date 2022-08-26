def printRepeating(arr):
    size = len(arr)
    i = 0
    print("Repeating elements :: ")
    while i < size:
        j = i + 1
        while j < size:
            if arr[i]==arr[j]:
                print(arr[i])
            j+=1
        i+=1

if __name__ == '__main__':
    printRepeating([1,2,3,4,5,2,3,1,4,1])
