class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 3. Remove head
    def remove_head(self):
        if self.head is None:
            print("The list is Empty")
        else:
            self.head = self.head.next

    # 4. Remove at the end
    def remove_at_the_end(self):
        if self.head is None:
            print("The list is Empty")
            return

        # If there is only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        # Stop at the second-last node
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Print the list
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# User input function
def user_input():
    linked_list = LinkedList()

    while True:
        print("\n1. Insert at beginning")
        print("2. Insert at end")
        print("3. Remove head")
        print("4. Remove at end")
        print("5. Print list")
        print("6. Exit")

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
            linked_list.print_list()

        elif choice == 6:
            print("Program ended.")
            break

        else:
            print("Invalid choice!")


user_input()
