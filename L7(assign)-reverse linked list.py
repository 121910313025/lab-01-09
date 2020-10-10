#Reverse the linked list
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

    def nodesinReverse(self):
	temp = self.head

	if temp == None:
            print("Empty!")
	rev = []
	k = []

	while temp:
	    rev.append(temp.data)
	    temp = temp.next
	for i in range(len(rev)-1,-1,-1):
	    k.append(rev[i])
	print(k)
	

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
    k = int(input())
    LL.append(k)

print("Before: ")
LL.display()

print("New Reversed List: ")
LL.nodesinReverse()

