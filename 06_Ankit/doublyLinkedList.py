

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLInkedList:
   def __init__(self):
      self.head=None

   def insert_at_front(self,x):
           newNode=Node(x) 
           if self.head is None:
                self.head=newNode
                return


           newNode.next=self.head
           self.head.prev=newNode
           self.head=newNode
           

    #displaying the linked list data       
   def display(self):
           if self.head is None:
               return None
   
           curr=self.head
           while curr is not None:
               print(curr.data,end="-->")
               curr=curr.next   
           print('None')  

   def delete_at_end(self):    
        if self.head is None:
             return print("list is empty")  
        curr=self.head
        if curr.next is None :
             return None
        while curr.next is not None :
            curr =curr.next  

        curr.prev.next=None

   def delete_at_index(self,index):
        if self.head is None:
          print("List is empty.")
          return
        curr=self.head
        if index==1:
             self.head=self.head.next
             return
             
        for i in range(index-1):
             curr=curr.next
             if curr is None:
                  return print("index out of bound")
             
        if curr.next is not None:
            curr.next.prev = curr.prev
            
        if curr.prev is not None:
            curr.prev.next = curr.next

   def insert_at_index(self,x,index)  :
        curr=self.head
        newNode=Node(x)
        if index==1:
          self.insert_at_front(x)
          return

        newNode=Node(x) 
        curr=self.head 
        for i in range(index-1):
             curr=curr.next
             if curr is None:
                  print("invalid index")
                  return
        if curr.next is None:
             newNode.prev=curr
             curr.next=newNode     
        newNode.prev=curr.prev
        curr.prev.next=newNode
        newNode.next=curr
        
   def insert_at_end(self,x):
        if self.head is None:
             return
        newNode=Node(x)
        curr=self.head
        while curr.next is not None:
             curr=curr.next

        newNode.prev=curr
        curr.next=newNode    

              
if __name__ == '__main__':
    # The user simply create list
    list=DoublyLInkedList()
    list.insert_at_front(5) 
    list.insert_at_front(6)
    list.insert_at_front(7) 
    list.insert_at_front(8)  
    list.insert_at_index(100,100)
    list.insert_at_end(100)
    list.display()