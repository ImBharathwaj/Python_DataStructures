# def addUp(arr):


if __name__ == "__main__":
    arr = [[None]*3]*3
    for i in range(3):
        for j in range(3):
            arr[i][j] = j
    print(arr)
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += arr[i][j]
    print(sum)