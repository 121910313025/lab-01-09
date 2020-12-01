# program to print zigzag traversal of a binary tree using Recursion  
#121910313025 
# Binary tree node  
class Node:  
  
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Recursive Function to find height  
# of binary tree  
def heightOfTree(root):  
  
    if root == None: 
        return 0
    lheight = heightOfTree(root.left)  
    rheight = heightOfTree(root.right)  
    return max(lheight + 1, rheight + 1)  
  
# Function to print nodes from right to left  
def printRightToLeft(root, level):  
  
    if root == None: 
        return
      
    if level == 1:  
        print(root.data, end = " ")  
      
    elif level > 1: 
      
        printRightToLeft(root.right, level - 1)  
        printRightToLeft(root.left, level - 1)  
  
# Function to print nodes from left to right  
def printLeftToRight(root, level):  
  
    if root == None: 
        return
      
    if level == 1:  
        print(root.data, end = " ")
    elif level > 1:
        printLeftToRight(root.left, level - 1)
        printLeftToRight(root.right,level - 1)
# Function to print Reverse ZigZag of  
# a Binary tree  
def printZigZag(root):  
  
    # Flag is used to mark the  
    # change in level  
    flag = 0
      
    # Height of tree  
    height = heightOfTree(root)  
      
    for i in range(1, height + 1):  
      
        # If flag value is one print nodes from right to left  
        if flag == 1: 
          
            printRightToLeft(root, i)  
              
            # Mark flag as zero so that next time nodes are printed from left to right  
            flag = 0
         # If flag is zero print nodes  from left to right  
        elif flag == 0: 
          
            printLeftToRight(root, i)  
              
            # Mark flag as one so that next time nodes are printed from right to left  
            flag = 1
          
# Driver code  
if __name__ == "__main__":  
  
    root = Node(7)  
    root.left = Node(4)  
    root.right = Node(5)  
    root.left.left = Node(9)  
    root.right.right = Node(10)  
    root.left.left.left = Node(6)  
    root.left.left.right = Node(11)  
      
    printZigZag(root) 
        
