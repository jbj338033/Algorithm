for _ in range(int(input())):
    a=[i for i in list(map(int,input().split())) if i%2==0]
    print(sum(a),min(a))