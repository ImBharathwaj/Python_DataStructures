import inspect

# Know depth of the recurssion
# Using inspect module
def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe())) - 1


def fibonacci(n):
    print("{indent} fibonacci({n}) called".format(indent=" " * stack_depth(), n=n))
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    fibonacci(10)
