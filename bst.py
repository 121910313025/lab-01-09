class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BST:
  def __init__(self):
    self.root=None
  def insert(self,val):
    if self.root==None:
      self.root=Node(val)
      return
    cur=self.root
    while cur:
      if val>cur.data:
        if cur.right==None:
          cur.right=Node(val)
          return
        cur=cur.right
      else:
        if cur.left==None:
          cur.left=Node(val)
          return
        cur=cur.left   
  def inorder(self,node):
    if node:
      self.inorder(node.left)
      print(node.data)
      self.inorder(node.right)
    
l=list(map(int,input("Enter a list to convert it into a BST :").split(" ")))
tree=BST()
for i in l:
  tree.insert(i)
tree.inorder(tree.root)
