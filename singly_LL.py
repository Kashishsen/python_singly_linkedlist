# appending element in the singly linked list
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Single_linkedlist:
    def __init__(self):
        self.head=None  #head refer to first element address of ll ..initially there is no element so it is none   
    def append(self,data):
        new_node=Node(data)
       
        if not self.head: # sll is empty 
            self.head=new_node  # Now head is refering next value of first node
        else:
            curr=self.head  #sll is not empty
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def traverse(self):
        if not self.head:
            print("singly linkedlist is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val, end=" ")    
                curr=curr.next
            print()
sll=Single_linkedlist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()                        


