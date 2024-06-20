'''ip: 7262 sec
op: 2h:1m:2

testcase2:
ip:500
op:0h:8m:20s'''
n=7262
h=n/3600
n=n-(h*36000)
m=n/60
s=n -(m*60)
print(h,"h",":",m,"m",":",s,"s")