v=['a', 'e', 'i', 'o', 'u']
while 1:
    a=input()
    if a=='end':break
    if not 'a' in a and not 'e' in a and not 'i' in a and not 'o' in a and not 'u' in a:
        print(f'<{a}> is not acceptable.')
    else:
        consonants = 0
        vowels = 0
        last=0

        for i in a:
            if i in v:
                vowels+=1
                consonants=0
            else:
                consonants+=1
                vowels=0
            
            if vowels==3 or consonants==3:
                print(f'<{a}> is not acceptable.')
                break
                
            if last == i and i != 'e' and i != 'o':
                print(f'<{a}> is not acceptable.')
                break

            last=i
        else:
            print(f'<{a}> is acceptable.')