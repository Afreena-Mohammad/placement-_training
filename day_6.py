#ip:[4,8,2,4,4,8,4] 
#ip:[2,1,2,2]
#ip:[6,6,6,6,7]
'''a=list(map(int,input().split(",")))
max=0
b=len(a)//2
p=0
for i in a:
    if a.count(i)>max and a.count(i)>=b:
        max=a.count(i)
        p=i
        
print(p)'''
'''a=[4,8,2,4,4,4,8]
c=1
p=a[0]
for i in range(1,len(a)):
    if a[i]==p:
        c=c+1
    else:
        if c!=0:
            c=c-1
        if c==0:
            p=a[i]
print(p)'''
#ip:7 [0 5 3 6 7 2 1] print missing number
'''a=[1,2,4,5,0]
n=len(a)
b=sum(a)
n=n*(n+1)//2
print(n-b)
'''
#ip: 5 7 8 2 1 4
#ip: 7 5 2 8 4 1
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
            
        else:
             t=node(x)
             t.nxt=self.head
             self.head.prev=t
             self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def print_even_odd_sum_difference(self):
        even_sum = 0
        odd_sum = 0
        t = self.head

        while t is not None:
            if t.data % 2 == 0:
                even_sum += t.data
            else:
                odd_sum += t.data
            t = t.nxt

        difference = even_sum - odd_sum
        print(f"Difference between even and odd sums: {difference}")
    def evod(self,t,es,os):
        if t==None:
            return abs(es-os)
        if t.data%2==0:
            es=es+t.data
        else:
            os=os+t.data
        return self.evod(t.nxt,es,os)
    def pr(self,t,c):
        if t == None:
            return c
        def pnt(s,n,c1):
            if (s>=(n//2)+1):
                return 1
            if n%s==0:
                return 0
            return pnt(s+1,n)
        if pnt(2,t.data):
            c=c+1
        return self.pr(t.nxt,c)
        
l1=dll()
l1.head=node(7)
l1.tail=l1.head
l1.addback(8)
l1.addfront(5)
l1.addback(2)
l1.addback(1)
l1.addback(4)
l1.display()
l1.print_even_odd_sum_difference()
print(l1.evod(l1.head,0,0))
l1.pr()




    
        
        