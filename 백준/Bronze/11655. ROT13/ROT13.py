for i in input():
    if i.isalpha():
        if i.islower():
            print(chr((ord(i)-ord('a')+13)%26+ord('a')),end='')
        else:
            print(chr((ord(i)-ord('A')+13)%26+ord('A')),end='')
    else:
        print(i,end='')