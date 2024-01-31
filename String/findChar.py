def indexOf(text, char):
    for i in range(len(text)):
        if(text[i] == char):
            print(f"Found at {i}")
        else:
            pass

if __name__ == '__main__':
    indexOf("Greatest Of All Time".lower(), "t")
