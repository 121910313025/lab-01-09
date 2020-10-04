#121910313025
class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None
class Linkedlist:
    def _init_(self):
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    def iterate_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def search_item(self, val):
         for node in self.iterate_item():
             if val == node:
                 return True
         return False
items = Linkedlist()
items.append_item('Apple')
items.append_item('Orange')
items.append_item('Grapes')
items.append_item('Kiwi')
items.append_item('Mango')
if items.search_item('Kiwi'):
    print("True")
else:
    print("False")
