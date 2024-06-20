class Node:
    def __init__(self):
        self.d = {}
        self.flag = 0

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
                print("Prefix not found")
                return
        self.dfs(temp, prefix)

    def dfs(self, node, current_word):
        if node.flag == 1:
            print(current_word)
        for char, child in node.d.items():
            self.dfs(child, current_word + char)
            
    def print_all_prefixes(self, prefix):
        def dfs(node, current_word):
            if node.flag == 1:
                print(current_word)
            for char in sorted(node.d.keys()):
                dfs(node.d[char], current_word + char)
        
        temp = self.root
        for char in prefix:
            if char in temp.d:
                temp = temp.d[char]
            else:
                print("Prefix not found")
                return
        dfs(temp, prefix)
    
    def print_largest_prefix(self, prefix):
        temp = self.root
        largest_prefix = ""
        current_word = ""
        for char in prefix:
            if char in temp.d:
                current_word += char
                temp = temp.d[char]
            else:
                break
        while temp:
            if temp.flag == 1:
                largest_prefix = current_word
            if temp.d:
                next_char = max(temp.d.keys())
                current_word += next_char
                temp = temp.d[next_char]
            else:
                break
        if largest_prefix:
            print(largest_prefix)
        else:
            print("Prefix not found")

t1 = Trie()

n = int(input("Enter the number of operations: "))
for i in range(n):
    a, s = input().split()
    if a == '1':
        t1.insert(s)
    elif a == '2':
        print(t1.search(s))
    elif a == '3':
        t1.printprefix(s)
    elif a == '4':
        t1.print_all_prefixes(s)
    elif a == '5':
        t1.print_largest_prefix(s)
