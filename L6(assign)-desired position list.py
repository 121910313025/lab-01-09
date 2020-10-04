#121910313025
#Insert node at desired position of the list
class Node:
    def _init_(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedlist:
    def _init_(self):
        self.headval=None
#function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middleNode.nextval=NewNode

#print the linked list
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

list=SLinkedlist()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Thu")
list.headval.nextval=e2
e2.nextval=e3
list.Inbetween(list.headval.nextval,"Fri")
list.listprint()
