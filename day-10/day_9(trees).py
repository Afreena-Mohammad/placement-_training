class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        else:
            if x < root.data:
                root.left = self.create(root.left, x)
            else:
                root.right = self.create(root.right, x)
        return root

    def insert(self, x):
        self.root = self.create(self.root, x)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
    def height(self, root):
        if root is None:
            return -1
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1
    def depth(self, root, x, depth=0):
        if root is None:
            return -1  
        if root.data == x:
            return depth
        elif x < root.data:
            return self.depth(root.left, x, depth + 1)
        else:
            return self.depth(root.right, x, depth + 1)
        
    def sum_of_nodes(self, root):
        if root is None:
            return 0
        return root.data + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right)
    def add_eve(self,root):
        if root ==None:
            return 0
        if root.data%2==0:
            
            return root.data+self.add_eve(root.left)+self.add_eve(root.right)
        else:
            return self.add_eve(root.left)+self.add_eve(root.right)
    def add_odd(self,root):
        if root ==None:
            return 0
        if root.data%2!=0:
            
            return root.data+self.add_odd(root.left)+self.add_odd(root.right)
        else:
            return self.add_odd(root.left)+self.add_odd(root.right)
        
    def sum_even_odd_diff(self, root):
        if root is None:
            return 0, 0
        left_even_sum, left_odd_sum = self.sum_even_odd_diff(root.left)
        right_even_sum, right_odd_sum = self.sum_even_odd_diff(root.right)
        even_sum = left_even_sum + right_even_sum
        odd_sum = left_odd_sum + right_odd_sum
        if root.data % 2 == 0:
            even_sum += root.data
        else:
            odd_sum += root.data
        return even_sum, odd_sum

    def diff_even_odd_sum(self):
        even_sum, odd_sum = self.sum_even_odd_diff(self.root)
        return even_sum - odd_sum
    def high(self,root):
        if root ==None:
            return -1
        else:
            l_s=self.high(root.left)
            r_s=self.high(root.right)
        return max(l_s,r_s)+1
    
    def bal(self,root):
            return abs(self.high(root.left)-self.high(root.right))<=1
    def countLeafNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countLeafNodes(root.left) + self.countLeafNodes(root.right)
    def sumLeafNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        return self.sumLeafNodes(root.left) + self.sumLeafNodes(root.right)
    def searchNode(self, root, target):
        if root is None:
            return False
        if root.data == target:
            return True
        return self.searchNode(root.left, target) or self.searchNode(root.right, target)
    def left_view(self):
        def left_view_u(Node,level,nax_level):
            if Node is None:
                return
            if level>max_level[0]:
                print(Node.data,end=" ")
                max_level[0]=level
            left_view_u(Node.left,level+1,max_level)
            left_view_u(Node.right,level+1,max_level)
        max_level=[0]
        left_view_u(self.root,1,max_level)
        print()
    


    
        
    
        
        
            


t1 = Tree()
t1.insert(10)
t1.insert(5)
t1.insert(20)
t1.insert(1)
t1.insert(7)
t1.insert(6)
t1.insert(8)
t1.insert(25)

print("Inorder traversal:")
t1.inorder(t1.root)  
print("\nPreorder traversal:")
t1.preorder(t1.root)  
print("\nPostorder traversal:")
t1.postorder(t1.root)
print("\n height")
print(t1.height(t1.root))
print("\ndepth")
print(t1.depth(t1.root,20))
print("\nsum")
print(t1.sum_of_nodes(t1.root))
print("\n add even")
print(t1.add_eve(t1.root))
print("\n add odd")
print(t1.add_odd(t1.root))
print("\n difference between even and odd")
print(t1.diff_even_odd_sum())
print("\n height")
print(t1.high(t1.root))
print("\n balance")
print(t1.bal(t1.root))
print("\n countleaves")
print(t1.countLeafNodes(t1.root))
print("\n sum of the leaf node")
print(t1.sumLeafNodes(t1.root))
print("\n search a node")
print(t1.searchNode(t1.root,25))
print("\n left view")
print(t1.left_view())
 