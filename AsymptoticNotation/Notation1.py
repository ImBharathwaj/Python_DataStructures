# Asymptotic Notation #1
# Time complexity : O(n)
# Linear time
def func1(n):
    m = 0
    i = 0
    while i < n:
        m+=1
        i+=1
    return m

if __name__ == '__main__':
    print(func1(10))
