# Asymptotic Notation 5
# Time Complexity : O(log(n))
# Logarithmic Time

def func5(n):
    m = 0
    i = n
    while i > 0:
        m += 1
        i = i/2
    return m

if __name__ == '__main__':
    print(func5(10))
