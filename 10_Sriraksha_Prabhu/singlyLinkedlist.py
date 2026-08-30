class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self, data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        current=self.head

        while current.next !=None:
            current=current.next

        current.next=new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next



    def update(self,old_value,new_value):
        current=self.head
        while current is not None:
            if (current.data==old_value):
                current.data=new_value
                return 

            current=current.next


    def delete(self,value):
        current=self.head
        if(current ==None):

            return

        if(current.data==value):
            self.head = current.next
            return
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

people=LinkedList()
people.insert(10)
people.insert(15)
people.insert(20)
people.insert(25)
people.insert(30)
print("Before update and delete")
people.display()
people.update(25,35)
print("After update and before delete")
people.display()
people.delete(35)
print("After delete")
people.display()