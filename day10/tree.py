v=[]
from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            def recur(root, val):
                if val < root.val:
                    if root.left == None:
                        root.left = Node(val)
                        return
                    recur(root.left, val)
                elif val > root.val:
                    if root.right == None:
                        root.right = Node(val)
                        return
                    recur(root.right, val)
            recur(self.root, val)
    def traverse(self):
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            print(root.val, end=' ')
            inorder(root.right)
        def preorder(root):
            if root == None:
                return
            print(root.val, end=' ')
            preorder(root.left)
            preorder(root.right)
        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
            print(root.val, end=' ')
        print("inorder:", end=' ')
        inorder(self.root)
        print()
        print("preorder:", end=' ')
        preorder(self.root)
        print()
        print("postorder:", end=' ')
        postorder(self.root)
        print()
    def left_v(self,root,c):
        if root==None:
            return
        if c not in v:
            print("root.data",root.val)
            v.append(c)
        self.left_v(root.left,c+1)
        self.left_v(root.right,c+1)
    def rightt_v(self,root,c):
        if root==None:
            return
        if c not in v:
            print("root.data",root.val)
            v.append(c)
        self.left_v(root.right,c+1)
        self.left_v(root.left,c+1)
    



        

bst = BST()
bst.add(10)
bst.add(5)
bst.add(15)
bst.add(2)
bst.add(7)
bst.add(11)
bst.add(20)
bst.add(4)
bst.add(12)
bst.add(3)
bst.add(13)
bst.add(14)
bst.traverse()
bst.left_v(bst.root,0)
v=[]
print("`````````````````````````")
bst.rightt_v(bst.root,0)
print("``````````````````````````")
bst.top_v(bst.root)
print("``````````````````````````")
bst.bottom_v(bst.root)
