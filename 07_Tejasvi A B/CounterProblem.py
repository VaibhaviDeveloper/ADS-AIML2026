class Node:
    def __init__(self, person_id):
        self.id = person_id
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add person at the end of the queue
    def enqueue(self, person_id):
        new_node = Node(person_id)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Serve the person at the front
    def dequeue(self):
        if self.head is None:
            return None

        served_id = self.head.id
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return served_id

    # Display queue
    def display(self):
        current = self.head

        while current:
            print(current.id, end=" -> ")
            current = current.next

        print("None")


class FoodCounters:
    def __init__(self):
        self.counter1 = LinkedList()  # Odd IDs
        self.counter2 = LinkedList()  # Even IDs

    def add_person(self, person_id):
        if person_id % 2 == 1:
            self.counter1.enqueue(person_id)
        else:
            self.counter2.enqueue(person_id)

    def show_counters(self):
        print("Counter 1 (Odd IDs):")
        self.counter1.display()

        print("Counter 2 (Even IDs):")
        self.counter2.display()

    def serve_food(self):
        print("\nServing Food:")

        while self.counter1.head or self.counter2.head:

            # Serve odd ID from Counter 1
            if self.counter1.head:
                person = self.counter1.dequeue()
                print(f"Person {person} gets food from Counter 1")

            # Serve even ID from Counter 2
            if self.counter2.head:
                person = self.counter2.dequeue()
                print(f"Person {person} gets food from Counter 2")


# Main program
food_counters = FoodCounters()

n = int(input("Enter number of people: "))

print("Enter IDs in arrival order:")

for _ in range(n):
    person_id = int(input())
    food_counters.add_person(person_id)

print("\nQueues:")
food_counters.show_counters()

food_counters.serve_food()
