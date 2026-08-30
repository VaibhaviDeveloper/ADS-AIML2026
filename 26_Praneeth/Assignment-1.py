#food truck problem considering customers are fixed standing in a single line

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

# creating a linkedlist to store all customers
def create_linkedlist(values):
    if not values:
        return None
    head=Node(values[0])
    current=head
    for val in values[1:]:
        current.next=Node(val)
        current=current.next
    return head

#display customers in a line
def display_linkedlist(head):
    current=head
    if current is None:
        print("empty")
        return
    while current:
        print(current.data, end="->")
        current=current.next
    print("end")

# dividing customers alternatively, assuming least injustice
def split_linkedlist(head):
    if head is None:
        return None, None

    #dummy heads for better split
    dummy1=Node(0)
    dummy2=Node(0)
    temp1=dummy1
    temp2=dummy2

    current=head
    assign=True

    while current:
        next_node=current.next
        current.next=None
        if assign:
            temp1.next=current
            temp1=current
        else:
            temp2.next=current
            temp2=current
        assign=not assign
        current=next_node
    return dummy1.next, dummy2.next


# implementaion
if __name__=="__main__":
    customers=[1,2,3,4,5,6,7,8,9]
    ll=create_linkedlist(customers)
    display_linkedlist(ll)
    counter1, counter2=split_linkedlist(ll)
    print("counter-1:", counter1)
    print("counter2:", counter2)
    print("cutomers for truck 1:")
    display_linkedlist(counter1)
    print("customers for trcuk 2:")
    display_linkedlist(counter2)