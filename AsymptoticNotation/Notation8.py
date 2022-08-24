# Asymptotic Notation 8
# Time complexity : O(n*root(n)) = O(n^(3/2))

import math

def func8(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < math.sqrt(n):
            m+=1
            j+=1
        i+=1
    return m

if __name__ == '__main__':
    print(func8(10))
