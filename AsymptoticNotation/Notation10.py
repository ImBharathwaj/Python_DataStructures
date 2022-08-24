# Asymptotic Notation 
# Time Complexity : O(n(n+1)/2)
# O(n^2) Arithmetic progression

def func10(n):
    m = 0
    i = 0
    while i < n:
        j = i
        while j > 0:
            m+=1
            j-=1
        i+=1
    return m

if __name__ == '__main__':
    print(func10(10))
