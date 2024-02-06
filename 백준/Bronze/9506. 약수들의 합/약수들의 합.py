while True:
    n = int(input())

    if n == -1:
        break

    arr = []

    for i in range(1, n+1):
        if n % i == 0 and n != i:
            arr.append(i)
    
    if sum(arr) == n:
        print(f"{n} = {' + '.join(map(str, arr))}")
    else:
        print(f"{n} is NOT perfect.")