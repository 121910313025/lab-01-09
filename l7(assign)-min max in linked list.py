#Minimum and Maximum elements in the node
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
	#deleting first node function
    def minmaxElements(self):
	temp = self.head
	mi = self.head.data
	ma = self.head.data
	while temp:
	    if temp.data>ma:
		ma = temp.data
	    if temp.data<mi:
		mi = temo.data
	    temp = temp.next
	    print("Minimum is: ",mi)
	    print("Maximum is: ",ma)

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
    k = int(input())
    LL.append(k)

LL.display()

LL.minmaxElements()
