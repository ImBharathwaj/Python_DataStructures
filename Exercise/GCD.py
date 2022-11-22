class DS:
    @classmethod
    def GCD(cls, m, n):
        if m < n:
            return cls.GCD(n, m)
        if m % n == 0:
            return n
        return cls.GCD(n, m % n)

if __name__ == '__main__':
    ds = DS()
    print(ds.GCD(10,7))