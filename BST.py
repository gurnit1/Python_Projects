class Node(object):
    val = 0
    left = None
    right = None

    def __init__(self, val):
        self.val = val

class BST(object):
    def __init__(self):
        pass
    def insert(self, tree, insertVal):
        if tree is None:
            tree = Node(insertVal)
            return tree
        else:
            if tree.val > insertVal:
                tree.left = self.insert(tree.left, insertVal)
                return tree
            elif tree.val < insertVal:
                tree.right = self.insert(tree.right, insertVal)
                return  tree
    def height(self, tree):
        if tree is None:
            return -1
        return max(self.height(tree.left), self.height(tree.right)) +1

    def print(self, tree):
        if tree is not None:
            self.print(tree.left)
            print(tree.val)
            self.print(tree.right)


root = Node(10)
lChild = Node(5)
rChild = Node(11)

root.left = lChild
root.right = rChild

b = BST()


root = b.insert(root, 2)
root = b.insert(root, 3)
root = b.insert(root, 4)
print(b.height(root))
#print(root.val)
#print(root.left.val)
#print(root.right.val)
#print(root.left.left.val)

b.print(root)


