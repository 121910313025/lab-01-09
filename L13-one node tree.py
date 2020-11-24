#To create a single node in binary tree
#121910313025
#class
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    #print
    def PrintTree(self):
        print(self.data)
tree=Node(25)
#calling print function
tree.PrintTree()
