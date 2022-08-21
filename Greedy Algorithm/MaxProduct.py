class MaxProd:
    # @param A: list of integer
    # @return an integer
    @classmethod
    def maxP(cls, A):
        A = sorted(A)
        hi3 = A[-1] * A[-2] * A[-3]
        lo2hi1 = A[0] * A[1] * A[-1]

        return max(hi3, lo2hi1)


if __name__ == '__main__':
    mp = MaxProd()
    arr = [1, 2, 3, 4]
    print(mp.maxP(arr))
