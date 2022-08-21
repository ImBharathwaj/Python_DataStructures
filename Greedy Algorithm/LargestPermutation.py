class LargestPermutation:
    # @param A: list of integer
    # @param B: integer
    # @return a list of integer
    @classmethod
    def solve(cls, A, B):
        i = 0
        _max = len(A)  # 5
        d = {x: i for i, x in enumerate(A)}
        # [3,2,4,1,5]
        while B and i < len(A):
            j = d[_max] # initially 4
            # First iteration -> 0 == 4
            if i == j:
                pass
            else:
                B -= 1
                A[i], A[j] = A[j], A[i]
                d[A[i]], d[A[j]] = d[A[j]], d[A[i]]
            i += 1
            _max -= 1
        return A


if __name__ == '__main__':
    lp = LargestPermutation()
    arr = [3, 2, 4, 1, 5]
    b = 4
    print(lp.solve(arr, b))
