class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def traversal(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

#updation
    def update(self, old_data, new_data):
        current = self.head
        while current != None:
            if current.data == old_data:
                current.data = new_data
                break
            current = current.next

#deletion
    def deletion(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                if current.prev == None:
                    self.head = current.next
                    if self.head != None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next != None:
                        current.next.prev = current.prev
                break
            current = current.next

    def insert_at_position(self, position, data):
        if position < 1:
            print(f"Invalid position ({position})! Position must be >= 1.")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            if self.head != None:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        for i in range(position - 2):
            if current is None:
                print(f"Position {position} is out of range!")
                return
            current = current.next

        if current is None:
            print(f"Position {position} is out of range!")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next != None:
            current.next.prev = new_node
        current.next = new_node


my_list = DoublyLinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.insert(40)
my_list.update(20, 25)
my_list.deletion(30)
my_list.traversal()

print("\n Insert in Middle ")
my_list.insert_at_position(3, 99)
my_list.traversal()  

print("\n Insert at Head ")
my_list.insert_at_position(1, 5)
my_list.traversal()  

print("\n Insert at Tail ")
my_list.insert_at_position(6, 50)
my_list.traversal()  

print("\n Position Out of Range ")
my_list.insert_at_position(100, 500)

print("\n Invalid Position ")
my_list.insert_at_position(0, 77)

print("\n Delete Head ")
my_list.deletion(5)
my_list.traversal()  

print("\n Delete Tail ")
my_list.deletion(50)
my_list.traversal()     
