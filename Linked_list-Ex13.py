print("Post Order traversal")
class Node(object):
    def __init__(self,data_value):
        self.data_value = data_value
        self.left = None
        self.right = None
    def insert_left(self,child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
    def insert_right(self,child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child
    def postorder(self,node):
        res=[]
        if node:
            res = self.postorder(node.left)
            res = res + self.postorder(node.right)
            res.append(node.data_value)
        return res
#Root_Node
print("Create Root Node")
root = Node("Root_Node")

#tree_left
print("Create Tree_left")
tree_left = Node("Tree_left")
root.insert_left(tree_left)

#Tree_Right
print("Create tree_Right")
tree_right = Node("Tree_Right")
root.insert_right(tree_right)

#TreeLL
print("Create TreeLL")
treell = Node("treell")
tree_left.insert_left(treell)
print("*******Postorder Traversal****")
print(root.postorder(root))
