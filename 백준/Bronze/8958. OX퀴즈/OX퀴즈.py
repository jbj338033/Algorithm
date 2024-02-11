for _ in range(int(input())):
    total = 0
    cnt = 0

    for a in list(input()):
        if a == "O":
            total += 1 + cnt
            cnt += 1
        else:
            cnt = 0
    
    print(total)