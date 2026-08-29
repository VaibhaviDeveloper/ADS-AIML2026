class ListNode:
	def __init__(self, val: int):
		self.value = val
		self.next = None
		self.prev =None
def nomatchmsg(flag):
	if flag == 0:
		print("\nNo match found\n")
def insertnode(val: int, head, tail):
	newNode = ListNode(val)
	newNode.next = head
	head = newNode
	if head != None:
		newnewnode = head.prev if head.prev != None else head  #Wrong
		print("prev",newnewnode.value)
		print("curr",head.value)
	if tail == None:
		tail = newNode
	return head, tail
def traverse(val, head, tail):
	curr = head
	prev = None
	flag = 0
	while curr != None:
		if curr.value == val:
			flag = 1
			return curr, prev
		prev = curr
		curr = curr.next
	nomatchmsg(flag)
	return None, None
def insertafterfirstfoundnode(insertval: int, val: int, head, tail):
	curr, prev = traverse(val, head)
	if curr != None:
		temp=insertnode(insertval,head)
		temp.next=curr.next
		curr.next = temp
# Below doesn't work rn, fix later
#def insertafterlastfoundnode(insertval: int, val: int, head):
#	curr, prev = traverse(val, head)
#	while curr != None:
#		newcurr = curr
#		newprev = prev
#		curr, prev=traverse(val, curr.next)
#	temp=insertnode(insertval,head)
#	temp.next=newcurr.next
#	newcurr.next = temp
def popnode_head(head):
	nextnode = head
	nextnextnode = nextnode.next
	nextnextnode.prev = None
	head = nextnode.next
	return head
def displaylist(head, tail):
	end = head
	while end != None:
		print(f" {end.value} {"<== Head" if end == head else ("<== Tail" if end == tail else "")}")
		print(" ^")
		print(" |")
		print(" v")
		end = end.next
	print("End")
def displaylist_reverse(head, tail):
	end = tail
	while end != None:
		print(f" {end.value} {"<== Head" if end == head else ("<== Tail" if end == tail else "")}")
		print(" ^")
		print(" |")
		print(" v")
		end = end.prev
	print("End")
def traverse_till_hit(val: int, head):
	end = head
	flag=0
	while end != None:
		if end.value == val:
			print("",end.value,"<---")
			flag=1
		else:
			print("",end.value)
		print(" ^")
		print(" |")
		print(" v")
		end = end.next
	print("End")
	nomatchmsg(flag)
def deletefirstfoundnode(val: int, head):
		curr, prev = traverse(val, head)
		traverse_till_hit(val, head)
		flag=0
		if curr != None:
			prev.next = curr.next
			print(curr.value,"deleted.")
			flag=1
			return
		prev=curr			
		curr = curr.next
		print("End")
		nomatchmsg(flag)
def deletelastfoundnode(val: int, head):
		curr = head
		lastmatch=None
		prev=None
		traverse_till_hit(val, head)
		flag=0
		while curr != None:
			if curr.value == val:
				lastmatch=curr
				lastmatchprev=prev
				flag=1 if flag != 1 else flag
			prev=curr
			curr = curr.next
		nomatchmsg(flag)
		if flag == 1:
			lastmatchprev.next = lastmatch.next
def deleteallnode(val: int, head):
		curr = head
		traverse_till_hit(val, head)
		flag=0
		while curr != None:
			if curr.value == val:
				previous = curr.prev
				previous.next = curr.next
				print(curr.value,"deleted.")
				flag=1			
			curr = curr.next
		print("End")
		nomatchmsg(flag)
head = None
tail = None
head, tail = insertnode(5, head, tail)
head, tail = insertnode(7, head, tail)
head, tail = insertnode(6, head, tail)
head, tail = insertnode(7, head, tail)
head = popnode_head(head)
head, tail = insertnode(8,head, tail)
head, tail = insertnode(7, head, tail)
#displaylist_reverse(head, tail)
#deleteallnode(7,head)
#deletelastfoundnode(7,head)
#traverse_till_hit(5,head)
#insertafterlastfoundnode(2,7,head)
displaylist(head, tail)