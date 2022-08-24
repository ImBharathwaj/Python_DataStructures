# Asymptotic Notation 6
# Time Complexity : O(n^2) + O(n^2) = O(n^2)
# Quadratic growth with Square rate


def func7(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
                m += 1
                j += 1
        i += 1
    i = 0
    while i < n:
        k = 0
        while k < n:
                m += 1
                k += 1
        i += 1
    return m


if __name__ == '__main__':
    print(func7(10))
