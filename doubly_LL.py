class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class Doubly_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_At_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def append(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp    

    def insert_at_specificposi(self,val,pos) :
        new_node=Node(val)
        if pos==0:
            self.insert_At_head(val)
            return
        curr=self.head
        count=0
        while curr and count< pos-1:
            curr=curr.next
            count+=1
        if curr is None:
            print("position out of bound")
            return
        new_node.next=curr.next
        new_node.prev=curr
        if curr.next :
            curr.next.prev=new_node
        curr.next=new_node
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
        print()    
    def delete_at_head(self):

        if self.head is None:
            return
        else:
            self.head=self.head.next
            if self.head:
                self.head.prev=None
    def delete_last(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next       
        temp.prev.next=None


    def delete_in_between(self,pos):
        temp=self.head
        if pos==0:
            self.delete_at_head()
            return
        

        count=0
        while temp and count<pos-1:
            temp=temp.next
            count+=1
        if temp is None or temp.next is None:
            print("position out of bound") 
            return   
        if temp.next.next is not None:
            temp.next=temp.next.next
            temp.next.prev=temp  
        else:
            temp.next=None 




dll=Doubly_linkedlist()
dll.insert_At_head(40)
dll.append(10)
dll.append(100)
dll.append(400)
dll.append(500)

dll.traverse()
dll.delete_last()
dll.traverse()
dll.delete_at_head()
dll.traverse()
dll.delete_in_between(7)
dll.traverse()


