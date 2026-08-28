class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 2. Insert at end
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

    # 3. Remove head
    def remove_head(self):
        if self.head is None:
            print("The list is Empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # 4. Remove at the end
    def remove_at_the_end(self):
        if self.head is None:
            print("The list is Empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Print from beginning to end
    def print_forward(self):
        if self.head is None:
            print("The list is Empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Print from end to beginning
    def print_backward(self):
        if self.head is None:
            print("The list is Empty")
            return

        temp = self.head

        # Go to last node
        while temp.next:
            temp = temp.next

        # Move backward using prev
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# User input function
def user_input():

    linked_list = DoublyLinkedList()

    while True:

        print("\n1. Insert at beginning")
        print("2. Insert at end")
        print("3. Remove head")
        print("4. Remove at end")
        print("5. Print forward")
        print("6. Print backward")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            linked_list.insert_at_beginning(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            linked_list.insert_at_end(data)

        elif choice == 3:
            linked_list.remove_head()

        elif choice == 4:
            linked_list.remove_at_the_end()

        elif choice == 5:
            linked_list.print_forward()

        elif choice == 6:
            linked_list.print_backward()

        elif choice == 7:
            print("Program ended.")
            break

        else:
            print("Invalid choice!")


user_input()
