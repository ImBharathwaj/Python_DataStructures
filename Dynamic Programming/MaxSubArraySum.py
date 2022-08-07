# Kadane's Algorithm
def maxSubArraySum(arr):
    size = len(arr)
    max = 0
    maxEndingHere = 0
    i = 0
    while i < size:
        maxEndingHere = maxEndingHere + arr[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
        if max < maxEndingHere:
            max = maxEndingHere
        i += 1
    return max


if __name__ == '__main__':
    arr = [2, -10, 11, 3, 4, -5, 1]
    print(maxSubArraySum(arr))
