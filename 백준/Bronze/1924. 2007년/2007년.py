import calendar
x,y=map(int,input().split())
print({0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}[calendar.weekday(2007,x,y)])