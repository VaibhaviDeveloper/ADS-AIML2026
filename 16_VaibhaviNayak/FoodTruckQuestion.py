class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=None
def insertAtEnd(data):
    global head
    newNode=Node(data)
    if head is None:
        head=newNode
    else:
        curr=head
        while curr.next is not None:
            curr=curr.next
        curr.next=newNode

def traverse():
    if head is None:
        return
    else:
        curr=head
        while curr is not None:
            print(curr.data)
            curr=curr.next

def shopArrangement():
    global head
    pos=0
    curr=head
    while curr is not None:
        pos+=1
        curr=curr.next
    
    curr=head
    mid=pos//2
    for i in range(mid-1):
        curr=curr.next

    head1=head
    last1=curr
    head2=last1.next
    
    last1.next=None

    prev=None
    curr=head2
   
    while curr is not None:
         next=curr.next
         
         curr.next=prev
         prev=curr
         curr=next

    head2=prev
    print("First List:")
    curr = head1
    while curr is not None:
        print(curr.data)
        curr = curr.next

    print("Second List:")
    curr = head2
    while curr is not None:
        print(curr.data)
        curr=curr.next

    
        

    

insertAtEnd(10)
insertAtEnd(20)
insertAtEnd(30)
insertAtEnd(40)
insertAtEnd(50)
traverse()
print("******************")
traverse()
print("*****************")
shopArrangement()
