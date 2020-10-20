#121910313025
#to create a double linked list and insert node at end
#create class
class Node:
    def __init__(self,data):
        self.data=data;
        self.previous=None;
        self.next=None;
class InsertEnd:
    def __init__(self):
        self.head=None;
        self.tail=None;
    def addAtEnd(self, data):    
        #Create a new node    
        newNode = Node(data);    
        #If list is empty    
        if(self.head == None):    
            #Both head and tail will point to newNode    
            self.head = self.tail = newNode;    
            #head's previous will point to None    
            self.head.previous = None;    
            #tail's next will point to None, as it is the last node of the list    
            self.tail.next = None;
        else:
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode;    
            #newNode's previous will point to tail    
            newNode.previous = self.tail;    
            #newNode will become new tail    
            self.tail = newNode;    
            #As it is last node, tail's next will point to None    
            self.tail.next = None;
    def display(self):
        current=self.head;
        if(self.head == None):
            print("list is empty");
            return;
        print("Nodes of double linked list: ");
        while(current != None):
            print(current.data),;
            current=current.next;
dList =InsertEnd()
dList.addAtEnd(10);
dList.display();
dList.addAtEnd(20);
dList.display();
dList.addAtEnd(30);
dList.display();
dList.addAtEnd(40);
dList.display();
dList.addAtEnd(50);
dList.display();
