#121910313025
#inserting a node at any position in doubly linked list   
class Node:    
    def _init_(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class InsertMid:    
    #Represent the head and tail of the doubly linked list    
    def _init_(self):    
        self.head = None;    
        self.tail = None;    
        self.size = 0;    
            
    #addNode() will add a node to the list    
    def addNode(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
                
            self.head = self.tail = newNode;    
               
            self.head.previous = None;    
               
            self.tail.next = None;    
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode;    
               
            newNode.previous = self.tail;    
               
            self.tail = newNode;    
               
            self.tail.next = None;    
         
        self.size = self.size + 1;    
            
    #addInMid() will add a node to the middle of the list    
    def addInMid(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
                
            self.head = self.tail = newNode;    
               
            self.head.previous = None;    
                
            self.tail.next = None;    
        else:    
            #current will point to head    
            current = self.head;
            #Store the mid position of the list    
            mid = (self.size//2) if(self.size % 2 == 0)  else ((self.size+1)//2);    
                
            #Iterate through list till current points to mid position    
            for i in range(1, mid):    
                current = current.next;    
                    
            #Node temp will point to node next to current    
            temp = current.next;    
            temp.previous = current;    
                
            #newNode will be added between current and temp    
            current.next = newNode;    
            newNode.previous = current;    
            newNode.next = temp;    
            temp.previous = newNode;    
        self.size = self.size + 1;    
                
    #display() will print out the nodes of the list    
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        while(current != None):    
            #Prints each node by incrementing pointer.    
            print(current.data),    
            current = current.next;    
                
        print();    
            
dList = InsertMid();
#Add nodes to the list    
dList.addNode(10);    
dList.addNode(20);    
     
print("Original list: ");    
dList.display();    
     
#Adding node '3' in the middle    
dList.addInMid(30);    
print( "Updated List: ");    
dList.display();    
     
#Adding node '4' in the middle    
dList.addInMid(40);    
print("Updated List: ");    
dList.display();    
     
#Adding node '5' in the middle    
dList.addInMid(50);    
print("Updated List: ");
dList.display();
