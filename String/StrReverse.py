def reverseItr(text):
    dum = ""
    for i in text[::-1]:
        dum += i
    return dum


def recurReverse(text):
    if len(text) == 0:
        return

    temp = text[0]
    recurReverse(text[1:])
    print(temp, end="")


def reversePtr(text):
    n = len(text)
    i, j = 0, n - 1

    while i < j:
        text[i], text[j] = text[j], text[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    text = "Nothing"
    reverseItr(text)
    print(text[::-1])
    recurReverse(text)
    print()
    str  = list(text)
    reversePtr(str)
    print(str)