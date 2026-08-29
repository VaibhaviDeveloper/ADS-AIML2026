# Singly Linked List - All Common Operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 3. Insert at a specific position
    # Position starts from 1
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_beginning(data)
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
        temp.next = new_node

    # 4. Insert after a given value
    def insert_after_value(self, value, data):
        temp = self.head

        while temp:
            if temp.data == value:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("Value not found")

    # 5. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 6. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # 7. Delete by value
    def delete_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        # If first node contains value
        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    # 8. Delete from a specific position
    # Position starts from 1
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for _ in range(position - 2):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    # 9. Search for a value
    def search(self, value):
        temp = self.head
        position = 1

        while temp:
            if temp.data == value:
                return position

            temp = temp.next
            position += 1

        return -1

    # 10. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 11. Count nodes
    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # 12. Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 13. Find middle node
    # Uses slow and fast pointers
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # 14. Find nth node from end
    def nth_from_end(self, n):
        if n <= 0:
            return None

        first = self.head
        second = self.head

        # Move first pointer n nodes ahead
        for _ in range(n):
            if first is None:
                return None
            first = first.next

        # Move both pointers
        while first:
            first = first.next
            second = second.next

        return second.data


# --------------------------------------------------
# Example Usage
# --------------------------------------------------

ll = SinglyLinkedList()

# Insert operations
ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insert_end(20)
ll.insert_end(30)

print("Initial list:")
ll.display()
# 5 -> 10 -> 20 -> 30 -> None

# Insert at position
ll.insert_at_position(15, 3)

print("\nAfter inserting 15 at position 3:")
ll.display()
# 5 -> 10 -> 15 -> 20 -> 30 -> None

# Insert after value
ll.insert_after_value(20, 25)

print("\nAfter inserting 25 after 20:")
ll.display()
# 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> None

# Search
print("\nPosition of 20:", ll.search(20))

# Count
print("Number of nodes:", ll.count())

# Delete beginning
ll.delete_beginning()

print("\nAfter deleting first node:")
ll.display()

# Delete end
ll.delete_end()

print("\nAfter deleting last node:")
ll.display()

# Delete by value
ll.delete_value(20)

print("\nAfter deleting value 20:")
ll.display()

# Delete at position
ll.delete_at_position(2)

print("\nAfter deleting position 2:")
ll.display()

# Find middle
print("\nMiddle node:", ll.find_middle())

# Find nth node from end
print("2nd node from end:", ll.nth_from_end(2))

# Reverse
ll.reverse()

print("\nAfter reversing:")
ll.display()
