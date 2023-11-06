print("Preorder traversal")
class Node(object):
    def __init__(self,data_value):
        self.data_value = data_value
        self.left = None
        self.right = None
    def insert_left(self,child):
        if self.left is None:
            self.left = child
        else:
            child.left - self.left
            self.left = child
    def insert_right(self,child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child
    def preorder(self,node):
        res=[]
        if  node:
            res.append(node.data_value)
            res = res + self.preorder(node.left)
            res = res + self.preorder(node.right)
        return res
#Root_Node
print("Create Root Node")
root = Node("Root_Node")

#Tree_Left
print("Create Tree_Left")
tree_left = Node("Tree_left")
root.insert_left(tree_left)

#Tree_Right
print("Create Tree_Right")
tree_right = Node("tree_Right")
root.insert_right(tree_right)

#TreeLL
print("Create TreeLL")
treell = Node("TreeLL")
tree_left.insert_left(treell)
print("*****Preorder traversal****")
print(root.preorder(root))

