class Interval:
    # @param A: list of list of integer
    # @return an integer
    @classmethod
    def solve(cls, arr):
        arr.sort(key=lambda x: x[1])
        prev_s, prev_e = arr[0]
        count = 1
        for s, e in arr:
            if s <= prev_e:
                print(s, '->', prev_e)
                pass
            else:
                prev_s, prev_e = s, e
                count += 1
        return count


if __name__ == '__main__':
    i = Interval()
    A = [[1, 2], [2, 10], [4, 6]]
    i.solve(A)
