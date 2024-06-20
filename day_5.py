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
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def linear_search(self,x):
        h=self.head
        t=self.tail
        while(h!=None and t!=None and h!=t.nxt):
            if h.data==x:
                return 'found'
            if t.data==x:
                return 'found'
            h=h.nxt
            t=t.prev
        if(h==t and h==x and h!=None):          
            return 'found'
        else:
            return 'not found'
    def lenevod(self):
        h=self.head
        t=self.head
        while(h!=t and h!=t.nxt):
            h=h.nxt
            t=t.prev
        if h==t:
            return "odd"
        else:
            return "even"
    def palindrome(self):
        h=self.head
        t=self.head
        while(h!=t and h!=t.nxt):
            if h.data!=t.data:
                return 0
            h=h.nxt
            t=t.prev
        return 1
    def halff(self):
        f=self.head
        s=self.head
        while h!=None:
            f=f.nxt.nxt
            s=s.nxt
        s.tail.nxt=self.head
        s.head.prev=self.tail
        t=self.prev
        t.nxt=None
        self.prev=None
        self.head=None
        self.head=self
        self.tail=t
        
            
            
            
            
        
    
    
    
        
        
        
                
            
            
            
        
        
        
l1=dll()
l1.head=node(5)
l1.tail=l1.head
l1.addback(20)
l1.addfront(30)
l1.addback(50)
l1.addback(60)
l1.addfront(80)
l1.display()
l1.rev_display()
print(l1.linear_search(50))
print(l1.lenevod())
print(l1.palindrome())

        
        