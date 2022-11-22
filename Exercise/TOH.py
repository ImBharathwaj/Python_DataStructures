class DS:
    @classmethod
    def towerOfHanoi(cls, num, src, dst, temp):
        if num < 1:
            return
        cls.towerOfHanoi(num - 1, src, temp, dst)
        print("Move ", num, " disk from peg ", src, " to peg ", dst)
        cls.towerOfHanoi(num - 1, temp, dst, src)

    @classmethod
    def main(cls):
        num = 3
        print("sequence of moves in the Tower of Hanoi are :")
        cls.towerOfHanoi(num, 'A','B','C')

if __name__ == '__main__':
    ds = DS
    ds.main()
