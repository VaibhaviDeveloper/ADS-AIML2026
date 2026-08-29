class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # 2. Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Go to the last node
        while temp.next:
            temp = temp.next

        # Traverse backwards
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    # 3. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 4. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # 5. Insert at a specific position
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # 6. Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    # 7. Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # 8. Delete from a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.delete_from_beginning()
            return

        temp = self.head

        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # 9. Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # 10. Search an element
    def search(self, value):
        temp = self.head
        position = 1

        while temp:
            if temp.data == value:
                print(f"{value} found at position {position}")
                return True

            temp = temp.next
            position += 1

        print(f"{value} not found")
        return False

    # 11. Count number of nodes
    def count(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    # 12. Update a node
    def update(self, old_value, new_value):
        temp = self.head

        while temp:
            if temp.data == old_value:
                temp.data = new_value
                print("Value updated successfully")
                return

            temp = temp.next

        print("Value not found")

    # 13. Reverse the doubly linked list
    def reverse(self):
        temp = self.head

        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev

        if self.head:
            self.head = self.head.prev

    # 14. Find first element
    def first(self):
        if self.head:
            print("First element:", self.head.data)
        else:
            print("List is empty")

    # 15. Find last element
    def last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        print("Last element:", temp.data)

    # 16. Check if list is empty
    def is_empty(self):
        return self.head is None


# ------------------------------------
# Example
# ------------------------------------

dll = DoublyLinkedList()

# Insert operations
dll.insert_at_beginning(20)
dll.insert_at_beginning(10)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Doubly Linked List:")
dll.display_forward()

print("\nBackward:")
dll.display_backward()

# Insert at position
dll.insert_at_position(25, 3)

print("\nAfter inserting 25 at position 3:")
dll.display_forward()

# Search
print("\nSearch:")
dll.search(30)
dll.search(100)

# Count
print("\nNumber of nodes:", dll.count())

# First and last
dll.first()
dll.last()

# Update
dll.update(25, 35)

print("\nAfter updating 25 to 35:")
dll.display_forward()

# Delete by value
dll.delete_by_value(35)

print("\nAfter deleting 35:")
dll.display_forward()

# Delete from beginning
dll.delete_from_beginning()

print("\nAfter deleting from beginning:")
dll.display_forward()

# Delete from end
dll.delete_from_end()

print("\nAfter deleting from end:")
dll.display_forward()

# Delete from position
dll.delete_at_position(2)

print("\nAfter deleting position 2:")
dll.display_forward()

# Reverse
dll.reverse()

print("\nAfter reversing:")
dll.display_forward()

print("\nBackward after reversing:")
dll.display_backward()
