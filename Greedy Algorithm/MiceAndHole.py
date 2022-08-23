class MiceAndHole:
    # @param A : list of integer
    # @param B : list of integer
    # @return an integer
    @classmethod
    def mice(cls, A, B):
        A.sort()
        B.sort()

        ans = 0
        for a, b in zip(A, B):
            ans = max(ans, abs(a-b))
        return ans

if __name__ == '__main__':
    mh = MiceAndHole()
    A = [3, -2, 0]
    B = [-4, 2, 4]
    print(mh.mice(A, B))
