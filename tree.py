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
#Root_Node
print("Create Root Node")
root = Node("Root_Node")
print("Value of Root = ",root.data_value,"left =",root.left,"right = ",root.right)

#Tree_Left
print("Create Tree_Left")
tree_left = Node("Tree_Left")
root.insert_left(tree_left)
print("Value of Node =",tree_left.data_value,"left =",tree_left.left,"right =",tree_left.right)
print("Value of Root = ",root.data_value,"left =",root.left,"right = ",root.right)

#Tree_Right
print("Create Tree_Right")
tree_right = Node("Tree_Right")
root.insert_right(tree_right)
print("Value of Node =",tree_right.data_value,"left = ",tree_right.left,"right =",tree_right.right)
print("Value of Root = ",root.data_value,"left =",root.left,"right = ",root.right)
#TreeLL
print("Create TreeLL")
treeLL = Node("TreeLL")
tree_left.insert_left(treeLL)
print("Value of Node = ",treeLL.data_value,"left =",treeLL.left, "right = ",treeLL.right)
print("Value of Node = ",tree_left.data_value,"left =",tree_left.left,"right= ",tree_left.right)
print("Value of Root =",root.data_value,"left =",root.left,"right =",root.right)
