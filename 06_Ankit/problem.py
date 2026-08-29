class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class FoodTruck:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        
        curr = self.head
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def shopArrangement(self):
        # Edge case: If list is empty or has only 1 node, it can't be split
        if self.head is None or self.head.next is None:
            print("List is too short to arrange.")
            return

        # 1. Find the total length
        pos = 0
        curr = self.head
        while curr is not None:
            pos += 1
            curr = curr.next
    
        # 2. Traverse to the midpoint
        curr = self.head
        mid = pos // 2
        for i in range(mid - 1):
            curr = curr.next

        # 3. Split the list into two halves
        head1 = self.head
        last1 = curr
        head2 = last1.next
    
        last1.next = None # Sever the connection

        # 4. Reverse the second half (head2)
        prev = None
        curr = head2
    
        while curr is not None:
            next_node = curr.next
            
            curr.next = prev
            prev = curr
            curr = next_node

        head2 = prev

        # 5. Print the results
        print("\nFirst List:")
        curr = head1
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

        print("\nSecond List:")
        curr = head2
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")