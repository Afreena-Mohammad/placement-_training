''' consider a year has 360 days a month has 30 days in a month ,a week as 6 days
total number of days =65476
how many years
how many months
how many weeks
how many days are left'''
n=int(input())
a=n//360
k=n-a*360
b=n//30

c=n-(b*30)
print(a,b,c,k)
