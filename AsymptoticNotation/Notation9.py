# Asymptotic Notation 9
# Time Complexity : O(log(n))
# Logarithmic time
# Problem space is divided into half

def func9(n):
    m = 0
    i = n
    while i > 0:
        j = 0
        while j < i:
            m+=1
            j += 1
        i /= 2
    return m

if __name__ == '__main__':
    print(func9(10))
