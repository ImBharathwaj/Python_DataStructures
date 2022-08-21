class Solution:
    # @param A : list of integer
    # @return an integer
    @classmethod
    def bulb(cls, arr):
        # Intilize cost with value 0
        cost = 0
        for b in arr:
            if cost % 2 == 0:
                b = b
            else:
                b = not b
            if b % 2 == 1:
                continue
            else:
                cost += 1
        return cost


if __name__ == '__main__':
    s = Solution()
    A = [0, 1, 0, 1, 1, 0, 1, 1]
    print(s.bulb(A))
