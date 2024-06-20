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
    def right_view(self):
        def right_view_u(Node,level,max_level):
            if Node is None:
                return
            if level>max_level[0]:
                print(Node.data,end=" ")
                max_level[0]=level
            
            right_view_u(Node.right,level+1,max_level)
            right_view_u(Node.left,level+1,max_level)
        max_level=[0]
        right_view_u(self.root,1,max_level)
        print()     
    def top_view(self):
        def top_view_u(Node,level,hd,level_map,hp_map):
            if Node is None:
                return
            if hd not in hd_map or level<level_map[hd]:
                level_map[hd]=level
                hd_map[hd]=Node.data
            
            top_view_u(Node.left,level+1,hd-1,level_map,hd_map)
            top_view_u(Node.right,level+1,hd-1,level_map,hd_map)
        level_map={}
        hd_map={}
        top_view_u(self.root,0,0,level_map,hd_map)
        for hd in sorted(hd_map.keys()):
            print(hd_map[hd],end=" ")
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
print(t1.left_view())
print(t1.right_view())
print(t1.top_view())
