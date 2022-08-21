class MeetingRoom:
    # @param A: list of list of integer
    # @return an integer
    @classmethod
    def solve(cls, A):
        curr = 0
        _max = 0
        data = []
        for s, e in A:
            data.append((s, 1))
            data.append((e, -1))
        
        data.sort()
        for _, v in data:
            curr += v
            _max = max(_max, curr)
        return _max


if __name__ == '__main__':
    mr = MeetingRoom()
    arr = [[0, 30], [5, 10], [15, 20]]
    print(mr.solve(arr))
