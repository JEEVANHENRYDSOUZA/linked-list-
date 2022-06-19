# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    p=head
	q=head
	count=1
	while (count<=k):
		p=p.next
		count+=1
	if p is None:
		head.value=head.next.value
		head.next=head.next.next
		return	
	while(p.next is not None):
		p=p.next
		q=q.next
	q.next=q.next.next
	
