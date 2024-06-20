class node:
    def __intit__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False
    def search_prefix(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def print_all_prefixes(self,str):
        def fun():
            if t.flag==1:
                print(s)
            for i in t.d:
                fun(i,t.d[i],s+i)
            
        t=self.root
        s=""
        for i in str:
            if i in t.d:
                t=t.d[i]
            else:
                return
            fun(t)
        
            

t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if a=='1':
        t1.insert(s)
    if a=='2':
        print(t1.search(s))
    if a=='3':
        print(t1.search_prefix(s))
    if a=='4':
        print(t1.print_all_prefixes(s))
    
        