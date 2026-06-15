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
    def insertion(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current is not None and count<position:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current        
    def deletion(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("Node not found")

sll=Single_linkedlist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()
sll.insertion(40,2)
sll.traverse()
sll.deletion(40) 
sll.traverse() 
sll.deletion(60)
                     


