# Sorting Solution
# Time Complexity: O(n log n)
# Space Complexity: O(1)
def func_large(arr, size):
    arr.sort()
    return arr[-1]

# Traversing Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def largest(arr, size):
    max = arr[0]
    for i in range(size):
        if(max < arr[i]):
            max = arr[i]
    return max

# Sorting Solution
# Time Complexity: O(n log n)
# Space Complexity: O(1)
def func_small(arr, size):
    arr.sort()
    return arr[0]

# Traversing Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def smallest(arr, size):
    small = arr[0]
    for i in range(size):
        if(small > arr[i]):
            small = arr[i]
    return small

if __name__ == '__main__':
    arr = [20,13,44,41,4,1,14,42,525,7, -91]
    print(largest(arr,len(arr)))
    print(smallest(arr,len(arr)))