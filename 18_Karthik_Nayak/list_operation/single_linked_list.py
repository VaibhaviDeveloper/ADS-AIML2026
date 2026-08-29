class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node    
    def traversal(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
    

#updation
    def update(self,old_data,new_data):
        current=self.head
        while current!=None:
            if current.data==old_data:
                current.data=new_data
                break
            current=current.next    
#deletion
    def deletion(self,target):
        prev=None
        current=self.head
        while current!=None:
            if current.data==target:
                if prev==None:
                    self.head=self.head.next
                    break
                else:
                    prev.next=current.next
                break
            prev=current
            current=current.next    

    def insert_at_position(self, position, data):
        # Edge case 1: invalid position (less than 1)
        if position < 1:
            print(f"Invalid position ({position})! Position must be >= 1.")
            return

        new_node = Node(data)

        # Edge case 2: inserting at the head (position 1)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to the (position - 1)th node
        current = self.head
        for i in range(position - 2):
            if current is None:
                print(f"Position {position} is out of range!")
                return
            current = current.next

        # Check if position exceeds list length + 1
        if current is None:
            print(f"Position {position} is out of range!")
            return

        # Link new node into the chain
        new_node.next = current.next
        current.next = new_node


# --- Testing All Singly Linked List Operations ---
my_list = LinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.insert(40)
my_list.update(20, 25)
my_list.deletion(30)
# Base list: 10 -> 25 -> 40 (Length = 3)

print("=== Base List ===")
my_list.traversal()

print("\n--- Test 1: Insert in Middle - insert_at_position(3, 99) ---")
my_list.insert_at_position(3, 99)
my_list.traversal()  # Expected: 10 -> 25 -> 99 -> 40

print("\n--- Test 2: Insert at Head - insert_at_position(1, 5) ---")
my_list.insert_at_position(1, 5)
my_list.traversal()  # Expected: 5 -> 10 -> 25 -> 99 -> 40

print("\n--- Test 3: Insert at Tail (position = length + 1 = 6) ---")
my_list.insert_at_position(6, 50)
my_list.traversal()  # Expected: 5 -> 10 -> 25 -> 99 -> 40 -> 50

print("\n--- Test 4: Position Out of Range - insert_at_position(100, 500) ---")
my_list.insert_at_position(100, 500)

print("\n--- Test 5: Invalid Position - insert_at_position(0, 77) ---")
my_list.insert_at_position(0, 77)