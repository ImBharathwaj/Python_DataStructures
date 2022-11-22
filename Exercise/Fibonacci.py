class DS:
    @classmethod
    def fibonacci(cls, n):
        if n <= 1:
            return n
        return cls.fibonacci(n-1) + cls.fibonacci(n-2)

if __name__ == '__main__':
    ds = DS()
    print(ds.fibonacci(10))