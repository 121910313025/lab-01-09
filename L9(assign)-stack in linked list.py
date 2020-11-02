#Implement stack operation through singly linked list
#121910313025
class Node:
	def _init_(self,data):
		self.data = data
		self.next = None
class Stack:
	def _init_(self):
		self.head = None
		self.tail = None
	def push(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	def peek(self):
		l = self.tail.data
		return l
	def pop(self):
		if self.head is None:
			print("UNDERFLOW")
		else:
			prev = None
			cur = self.head
			while cur.next:
				prev = cur
				cur = cur.next
			prev.next = None
			cur = None
			self.tail = prev
	#printing elements
	def displayStack(self):
		print("Stack: ")
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()
	
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.displayStack()
print(s.peek())
s.pop()
s.displayStack()
