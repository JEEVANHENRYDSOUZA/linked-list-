# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode=linkedList
	while currentNode is not None:
		newDistinct=currentNode
		while newDistinct is not None and currentNode.value==newDistinct.value:
			newDistinct=newDistinct.next
		currentNode.next=newDistinct
	    currentNode=newDistinct
	return 	linkedList
