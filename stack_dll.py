class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next  
        print()    
    def pop(self):
        if self.head.next is None:
            self.head=None
            self.tail=None
            return
        
        self.tail=self.tail.prev 
        self.tail.next=None
class queue:
    def __init__(self):
        
        self.head=None
        self.tail=None
    def enqueue(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
    def dequeue(self):
        if self.head.next is None:
            self.head=None
            self.tail=None
            return
        self.head.next.prev=None
        self.head=self.head.next  
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next  
        print()                 
sd=queue()
sd.enqueue(10)
sd.enqueue(20)
sd.enqueue(30)  
sd.traverse()
sd.dequeue()      
sd.traverse()
sd.dequeue()
sd.traverse()
sd.dequeue()
sd.traverse()



                