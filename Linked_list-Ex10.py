class Tree:
    def __init__(self,data):
        self.tree = [data,[],[]]
    def left_subtree(self,branch):
        left_list = self.tree.pop(1)
        if len(left_list) > 1:
            branch.tree[1]=left_list
            self.tree.insert(1,branch.tree)
        else:
            self.tree.insert(1,branch.tree)
    def right_subtree(self,branch):
        right_list = self.tree.pop(2)
        if len(right_list)>1:
            branch.tree[2]=right_list
            self.tree.inster(2,branch.tree)
        else:
            self.tree.insert(2,branch.tree)

print("Create Root Node")
root = Tree("Root_node")
print("Value of Root =",root.tree)
print("Create Left Tree")
tree_left = Tree("Tree_left")
root.left_subtree(tree_left)
print("Value of Tree_left =",root.tree)
print("Create Right Tree")
tree_right = Tree("Tree_Right")
root.right_subtree(tree_right)
print("Value of Tree_Right = ",root.tree)
print("Create left Inbetween")
tree_inbtw = Tree("Tree left in between")
root.left_subtree(tree_inbtw)
print("Value of Tree_left = ",root.tree)
print("Create TreeLL")
treell = Tree("TreeLL")
tree_left.left_subtree(treell)
print("Value of Tree =",root.tree)
