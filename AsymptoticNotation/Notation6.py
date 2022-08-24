# Asymptotic Notation 6
# Time Complexity : O(n^3)
# Quadratic Equation with cube rate


def func6(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            k = 0
            while k < n:
                m += 1
                k += 1
            j += 1
        i += 1
    return m


if __name__ == '__main__':
    print(func6(10))
