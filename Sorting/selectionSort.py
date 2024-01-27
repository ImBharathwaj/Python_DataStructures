def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(n):
            if (arr[j] > arr[min]):
                min = j
    # if min != i:
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp
    
    for d in range(n):
        print(arr[d])


if __name__ == '__main__':
    arr=[7,4,10,8,3,1]
    selectionSort(arr)