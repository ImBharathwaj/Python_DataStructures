class Seats:
    # @param A: a string
    # @return an integer
    @classmethod
    def solve(cls, A):
        MOD = 100000003

        # All the indices of x is stored in this list
        crosses = [i for i, c in enumerate(A) if c == 'x']
        crosses = [(cross - i) for i, cross in enumerate(crosses)]

        n = len(crosses)
        if n == 0: return 0

        ans = float('inf')
        for segment_start in range(len(A)):
            total = 0
            for cross in crosses:
                total += abs(cross - segment_start)
                total %= MOD
            ans = min(ans, total% MOD)
        return ans

if __name__ == '__main__':
    s = Seats()
    print(s.solve('..x..x.'))
