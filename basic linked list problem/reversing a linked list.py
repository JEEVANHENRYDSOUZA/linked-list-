# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	previous,current=None,head
	while current is not None:
		nextNode=current.next
		current.next=previous
		previous=current
		current=nextNode
	return previous	
    
