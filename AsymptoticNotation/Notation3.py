# Asymptotic notation 3
# Time complexity : O(N+(N-1)+(N-2)+...) == O(N(N+1)/2) == O(n^2)
# Polynomial Growth
def func3(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < i:
            m += 1
            j += 1
        i += 1
    return m

if __name__ == '__main__':
    print(func3(10))
