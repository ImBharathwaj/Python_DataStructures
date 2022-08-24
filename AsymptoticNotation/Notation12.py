# Asymptotic Notation
# Time Complexity : O(n)
# Linear growth

def func12(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    return m


if __name__ == '__main__':
    print(func12(10))
