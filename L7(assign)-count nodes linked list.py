#count the number of nodes
#121910313025
#Node Class
class node:
    def _init_(self,data):
	self.data = data
	self.next = None
#Linked List Class
class LinkedList:
    def _init_(self):
	#initialization
	self.head = None
	self.tail = None
	#adding elements
    def append(self,data):
	new_node = node(data)
	if self.head == None or self.tail == None:
	    self.head = new_node
	    self.tail = new_node
	else:
	    self.tail.next = new_node
	    self.tail = new_node
	#printing elements
    def display(self):
	ele = []
	temp = self.head
	while temp:
	    ele.append(temp.data)
	    temp = temp.next
	print("Linked List: ",ele)
    def countElements(self):
	count = 0
	cur = self.head
	while cur:
	    count += 1
	    cur = cur.next
	print("Count is: ",count)


LL = LinkedList()
LL.append(10)
LL.append(20)
LL.append(30)
LL.append(40)
LL.append(50)

LL.display()
LL.countElements()
