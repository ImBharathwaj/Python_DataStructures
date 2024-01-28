def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()

if __name__ == '__main__':
    arr = [12,34,32,54,1,42,9,34]
    display(arr)
    bubbleSort(arr)
    display(arr)
