# Asymptotic Notation
# Time Complexity : O(n^3)

def func11(n):
    m = 0
    i = 0
    while i < n:
        j = i
        while j < n:
            k = j + 1
            while k < n:
                m+=1
                k+=1
            j+=1
        i+=1
    return m

if __name__ == '__main__':
    print(func11(10))
