class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

     #insert at front 
class LinkedLIst:    

    def __init__(self):
        self.head=None
    
    def insert_at_front(self,x):
        newNode=Node(x) 
        newNode.next=self.head
        self.head=newNode
        
   # insert at the end of the list
    def insert_at_end(self,x):
        newNode=Node(x)
        if self.head is None:
             self.head=newNode
             return

        current=self.head
        
        while current.next is not None:
            current=current.next   

        current.next=newNode
        


    #insert at given index
    def index(self,pos,x):
        if pos==1:
            self.insert_at_front(x)

        current =self.head
        newNode=Node(x)

        for i in range(1,pos-1):
            if current is None:
                break
            current=current.next
        if current is None:
            print(f"Cannot insert at position {pos}: Out of bounds.")
            return 

        newNode.next=current.next
        current.next=newNode


    #delete at the front
    def delete_at_front(self):
        if self.head is None:
            return print("list is empty")

        temp=self.head.next
        self.head=temp 
    # delete at the end     
    def delete_at_end(self):
        if self.head is None:
            return print("list is empty")
        current=self.head
        if current.next is None:
            current =None
        while current.next is not None and current.next.next is not None:
            current =current.next 

        current.next=None


    def delete_at_index(self,pos):
        if self.head is None:
            print("List is empty.")
            return

        if pos==1:
             return self.delete_at_front(x)

        current=self.head
        for i  in range(1,pos-1):
             if current is None or current.next is None:
                break
             current =current.next 
        if current is None or current.next is None:
            print(f"Cannot delete at position {pos}: Out of bounds.")
            return
        temp=current.next.next
        current.next=temp     

   #traversal of linked list
    def display(self):
        if self.head is None:
            return None

        current=self.head
        while current is not None:
            print(current.data,end="-->")
            current=current.next   
        print('None')

if __name__ == '__main__':
    # The user simply creat
    list=LinkedLIst()
    list.insert_at_front(5)
    
    


                   

             
             