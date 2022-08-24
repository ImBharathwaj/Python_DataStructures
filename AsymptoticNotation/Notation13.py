# Asymptotic Notation
# Time Complexity : O(n)

def func13(n):
    m = 0
    i = 1
    while i <= n:
        j = 0
        while j <= i:
            m += 1
            j += 1
        i *= 2
    return m


if __name__ == '__main__':
    print(func13(10))
