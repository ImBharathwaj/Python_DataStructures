# Asymptotic notation 4
# Time complexity : O(log(n))
# Logarithmic Time

def func4(n):
    m = 0
    i = 1
    while i < n:
        m+=1
        i*=2
    return m

if __name__ == '__main__':
    print(func4(10))
