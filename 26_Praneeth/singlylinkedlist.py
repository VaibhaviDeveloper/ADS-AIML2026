#single linkedlist 

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    # insert data at beginning
    def insert_begin(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return

        new_node.next=self.head
        self.head=new_node

    # delete data at beginning
    def delete_begin(self):
        if self.head is None:
            return
        self.head=self.head.next

    #insert data at middle
    def insert_middle(self, data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return 
        fast=self.head
        slow=self.head
        prev=None

        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        new_node.next=slow
        prev.next=new_node

    # delete at middle
    def delete_middle(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head=None
            return
        slow=self.head
        fast=self.head
        prev=None

        while fast.next is not None and fast.next.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev is None:
            self.head=slow.next
        else:
            prev.next=slow.next

    # insert value at end
    def insert_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def delete_end(self):
        if self.head is None:
            return 
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None 


    #traversal
    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")


ll=linkedlist()
ll.insert_begin(20)
ll.insert_begin(10)
ll.insert_end(21)
ll.insert_end(90)
ll.insert_middle(30)
ll.insert_middle(31)
ll.insert_middle(32)
ll.insert_begin(9)
ll.insert_end(99)
ll.delete_begin()
ll.delete_end()
ll.delete_end()
ll.delete_middle()
ll.delete_middle()
ll.display()