class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=None

def insertFront(data):
    global head
    newNode=Node(data)
    if head is None:
        head=newNode
    else:
        newNode.next=head
        head=newNode

def traverse():
    curr=head
    while curr is not None:
        print(curr.data)
        curr=curr.next

def insertEnd(data):
    global head
    newNode=Node(data)
    if head is None:
        head=newNode
    else:
        curr=head
        while curr.next is not None:
            curr=curr.next
        curr.next=newNode

def insertAtPosition(data, position):
    global head
    newNode=Node(data)
    if position==0:
        newNode.next=head
        head=newNode
    else:
        curr=head
        for i in range(position-1):
            curr=curr.next

        newNode.next=curr.next
        curr.next=newNode
        
def deleteAtFront():
    global head
    if head is None:
        return
    else:
        head=head.next

def deleteAtEnd():
    global head
    if head is None:
        return
    else:
        curr=head
        while curr.next.next !=None:
            curr=curr.next
        curr.next=None

def deleteAtPos(pos):
    global head
    if pos==0:
        head=head.next
    else:
        curr=head
        for i in range(pos-1):
            curr=curr.next
        curr.next=curr.next.next

def search(data):
    curr=head
    pos=0
    while curr is not None:
        if curr.data==data:
            print(data,pos)
            return
        else:
            pos+=1
            curr=curr.next
    return False

def reverse():
    global head
    prev,curr=None,head
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
        

insertFront(10)
insertFront(20)
insertEnd(30)
insertEnd(40)
insertFront(50)
insertAtPosition(60,3)
#deleteAtFront()
#deleteAtEnd()
#deleteAtPos(1)
insertEnd(90)
#search(90)
traverse()
print("**************")
reverse()
traverse()

    
    
   
    
