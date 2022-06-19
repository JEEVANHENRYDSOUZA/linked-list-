# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
	slowNode=head
	fastNode=head
	while fastNode is not None and fastNode.next is not None:
		fastNode=fastNode.next.next
		slowNode=slowNode.next
	reversedSecondHalfNode=reversedlinkedlist(slowNode)
	firstHalfNode=head
		
	while reversedSecondHalfNode is not None:
		if reversedSecondHalfNode.value != firstHalfNode.value:
			return False
		reversedSecondHalfNode=reversedSecondHalfNode.next
		firstHalfNode=firstHalfNode.next
	return True
		
		
		
		
		
		
		
		
		
def reversedlinkedlist(head):
	previousNode,currentNode=None,head
	while currentNode is not None:
		nextNode=currentNode.next
		currentNode.next=previousNode
		previousNode=currentNode
		currentNode=nextNode
	return previousNode
	
