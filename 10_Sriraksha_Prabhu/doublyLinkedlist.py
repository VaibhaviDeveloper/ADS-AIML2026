class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insertion_at_beginning(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            
    def insertion_at_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
            
    def insertion_at_middle(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            slow=self.head
            fast=self.head
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
            newnode.prev=slow.prev
            newnode.next=slow
            slow.prev.next=newnode
            slow.prev=newnode
            
    def display(self):
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            
    def display_reverse(self):
        if self.tail==None:
            print("empty")
        else:
            temp=self.tail
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.prev
                
    def delete_at_beginning(self):
        if self.head==None:
            print("empty")
        else:
            self.head=self.head.next
            self.head.prev=None
            
    def delete_at_end(self):
        if self.tail==None:
            print("empty")
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            
    def delete_at_middle(self):
        if self.head==None:
            print("empty")
        else:
            slow=self.head
            fast=self.head
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
            slow.prev.next=slow.next
            slow.next.prev=slow.prev
            
    def search(self,data):
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                if temp.data==data:
                    print("found")
                    break
                temp=temp.next
            else:
                print("not found")
            
    def insert_after(self,data,value):
        newnode=Node(data)
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                if temp.data==value:
                    newnode.prev=temp
                    newnode.next=temp.next
                    temp.next.prev=newnode
                    temp.next=newnode
                    break
                temp=temp.next
            else:
                print("not found")
            
    def insert_before(self,data,value):
        newnode=Node(data)
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                if temp.data==value:
                    newnode.prev=temp.prev
                    newnode.next=temp
                    temp.prev.next=newnode
                    temp.prev=newnode
                    break
                temp=temp.next
            else:
                print("not found")