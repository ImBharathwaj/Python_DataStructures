def checkPangram(s):
    List = []
    for i in range(26):
        List.append(False)

    for c in s.lower():
        if not c == ' ':
            List[ord(c) - ord('a')] = True

    for i in range(26):
        print(chr(i), List[i])

    for ch in List:
        if ch == False:
            return False
    return True

sentence = input('Enter a String : ')
sn = 'Sentence'

if(checkPangram(sentence)):
    print(sn.center(80,'-'))
    print('is a pangram'.center(80))
    print('-'*80)
else:
    print(sn.center(80,'-'))
    print('is not a pangram'.center(80))
    print('-'*80)
