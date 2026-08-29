#double linked list

class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None
class Dlinkedlist:
    def __init__(self):
        self.head=None

    def insert_begin(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def delete_begin(self):
        if self.head is None:
            return 
        self.head=self.head.next
        if self.head:
            self.head.prev=None

    def insert_middle(self, data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return 
        slow=self.head
        fast=self.head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        new_node.next=slow
        new_node.prev=slow.prev

        if slow.prev:
            slow.prev.next=new_node
        else:
            self.head=new_node
        slow.prev=new_node

    def delete_middle(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        if slow.prev:
            slow.prev.next=slow.next
        if slow.next:
            slow.next.prev=slow.prev

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        new_node.prev=temp
        temp.next=new_node

    def delete_end(self):
        if self.head is None:
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None

    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end="<->")
            temp=temp.next
        print("none")

    def display_reverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end="<->")
            temp=temp.prev
        print("None")

dll=Dlinkedlist()
dll.insert_begin(10)
dll.insert_begin(9)
dll.delete_begin()

dll.insert_end(100)
dll.insert_end(110)
dll.insert_middle(50)
dll.insert_middle(52)
dll.delete_end()
dll.insert_middle(51)
dll.delete_middle()
dll.display()
dll.display_reverse()