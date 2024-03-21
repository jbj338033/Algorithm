points = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}
credits = 0
total = 0
for i in range(int(input())):
    _,credit,point=input().split()
    credit=int(credit)
    point=points[point]

    credits += credit
    total += credit * point

a = round(total/credits+0.000000001,2)
print(f"{a}0" if len(str(a))==3 else a)