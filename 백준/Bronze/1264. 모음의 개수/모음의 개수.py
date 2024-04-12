while 1:
    a=input().lower()
    if a=='#': break
    print(a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u"))