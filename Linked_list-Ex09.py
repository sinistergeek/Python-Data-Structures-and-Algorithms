class Tree:
    def __init__(self,data):
        self.tree = [data, [],[]]
    def left_subtree(self,branch):
        left_list = self.tree.pop(1)
        self.tree.insert(1,branch.tree)
    def right_subtree(self,branch):
        right_list = self.tree.pop(2)
        self.tree.insert(2,branch.tree)
print("Create Root Node")
root = Tree("Root_node")
print("Value of Root =",root.tree)
print("Create Left Tree")
tree_left = Tree("True_left")
root.left_subtree(tree_left)
print("Value of Tree_Left = ",root.tree)
print("Create Right Tree")
tree_right = Tree("Tree_Right")
root.right_subtree(tree_right)
print("Value of Tree_Right = ",root.tree)
