
class Node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self, root, x):
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
    def inorder(root):
        if root:
            inorder(root.left)
            print(root.data, end=" ")
            inorder(root.right)
    def preorder(root):
        
        if root:
            print(root.data, end=" ")
            preorder(root.left)
            preorder(root.right)
    def postorder(root):
        
        
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.data,end=" ")
        
t1=tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,20)
t1.creat(t1.root,1)
t1.creat(t1.root,7)
t1.creat(t1.root,6)
t1.creat(t1.root,8)
t1.creat(t1.root,25)
print(t1.inorder(t1.root))
print(t1.preorder(t1.root))
print(t1.postorder(t1.root))


        