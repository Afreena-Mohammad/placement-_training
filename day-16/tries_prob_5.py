class Node:
    def __init__(self):
        self.d = {}  
        self.flag = 0  
        self.d1 = {}  

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root
        for i in word:
            if i not in temp.d:
                temp.d[i] = Node()
            temp = temp.d[i]
        temp.flag = 1  

    def search(self, word):
        temp = self.root
        for i in word:
            if i in temp.d:
                temp = temp.d[i]
            else:
                return False
        
        return temp.flag == 1
    
    def printprefix(self, prefix):
        temp = self.root
        for char in prefix:
            if char in temp.d:
                temp = temp.d[char]
            else:
                return False
        self.dfs(temp, prefix)

    def dfs(self, node, current_word):
        if node.flag == 1:
            print(current_word)
        for char, child in node.d.items():
            self.dfs(child, current_word + char)
            
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
                

t1 = Trie()

n = int(input())
for i in range(n):
    a,s = input().split()
    if(a=='1'):
        t1.insert(s)
    if (a=='2'):
        print(t1.search(s))
    if (a=='3'):
        print(t1.printprefix(s))
    if a=='4':
        print(t1.print_all_prefixes(s))