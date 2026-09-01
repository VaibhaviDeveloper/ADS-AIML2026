class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
        self.prev=None

head=None

def insertFront(data):
    global head
    newNode = Node(data)
    if head is None:
        head=newNode
    else:
        newNode.next=head
        head.prev=newNode
        head=newNode

def traverse():
    if head is None:
        print("List is empty")
        return
    else:
        curr=head
        while curr is not None:
            print(curr.data)
            curr=curr.next

def insertEnd(data):
    global head
    newNode=Node(data)
    if head is None:
        head=newNode
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=newNode
    newNode.prev=curr

def deleteFront():
    global head
    if head is None:
        return
    elif head.next is None:
        head=None
    else:
        curr=head.next
        curr.prev=None
        head.next=None
        head=curr

def deleteEnd():
    global head
    if head is None:
        return
    elif head.next is None:
        head=None
    else:
        curr=head
        while curr.next.next is not None:
            curr=curr.next
        curr.next=None

def insertAtPos(data,pos):
    newNode=Node(data)
    global head
    if pos==1:
        newNode.next=head
        if head is not None:
            head.prev=newNode
        head=newNode
    else:
        curr=head
        for i in range(2,pos):
            curr=curr.next
            if curr is None:
                print("Invalid Index , Node is Inserted at End")
                insertEnd(data)
                return
        if curr.next is None:
            insertEnd(data)
            return
        nextNode=curr.next
        curr.next=newNode
        newNode.prev=curr
        newNode.next=nextNode
        nextNode.prev=newNode

def deleteAtPos(pos):
    global head
    if pos==1:
        deleteFront()
    else:
        curr=head
        for i in range(1,pos-1):
            curr=curr.next
            if curr is None:
                print("Invalid Index")
                return

        if curr.next is None:
            deleteEnd()
            return
        nextNode=curr.next.next
        curr.next=nextNode
        nextNode.prev=curr    

    

insertFront(30)
insertFront(20)
insertFront(10)
insertEnd(40)
insertEnd(60)
deleteFront()
deleteEnd()
insertAtPos(50,2)
insertAtPos(100,3)
insertAtPos(100,100)
deleteAtPos(2)
deleteAtPos(3)
traverse()
