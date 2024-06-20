'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        

head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
t=head
while(t!=None):
    print(t.data)
    t=t.nxt'''
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
        
        
        
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addev(self):
        t=self.head
        s=0
        while(t!=None):
            if ((t.data)%2==0):
                s=s+(t.data)
            t=t.nxt
        print(s)
    def search(self,x):
        t=self.head
        while(t!=None):
            if t.data ==x:
                return "found"
            t=t.nxt
        return "not found"
    def findmiddle(self):
        t=self.head
        f=self.head
        while(f!=None and f.nxt):
            t=t.nxt
            f=f.nxt.nxt
        return t.data
    def lenev(self):
        t=self.head
        f=self.head
        while(f!=None and f.nxt):
            t=t.nxt
            f=f.nxt.nxt
        if f==None:
            print("even")
        else:
            print("odd")
    def len_long(self):#data is 1 2 3 4 7 8 9 3 4 5 length of logest sublist
        t=self.head
        c=1
        m=0
        while(t.nxt!=None):
            if (t.data==t.nxt.data-1):
                c=c+1
            else:
                if(c>m):
                    m=c
                c=1
            t=t.nxt
        if c>m:
            m=c
        print(m)
        
    def allpairs(self): # ip 6 7 4 8 4 2 0 1 print pairs
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
    def bubble(self):
        c=0
        T=self.head
        p=None
        while(T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if t.data>t.nxt.data:
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
                c=c+1
            if f==0:
                break
            p=t
            t=t.nxt
        print(c)
            
            
            
        
            
                


        
l1=sll()
l1.head=node(10)
l1.addback(70)
l1.addback(20)
l1.addfront(30)
l1.display()
print()
print(l1.search(10))
l1.addev()
print(l1.findmiddle())
print(l1.lenev())
print(l1.len_long())
print(l1.allpairs())
l1.bubble()
l1.display()

#data is 1 2 3 4 7 8 9 3 4 5 length of logest sublist
