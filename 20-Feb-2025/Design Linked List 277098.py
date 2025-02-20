# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=None, nextNode=None):
        self.val = val
        self.next = nextNode

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.length = 0
        self.printLinkedList()
    def get(self, index: int) -> int:

        i = index
        if not i<self.length:
            return -1

        current = self.dummy.next

        while i:
            current = current.next
            i-=1

        return current.val
        
        self.printLinkedList()


    def addAtHead(self, val: int) -> None:
        newHead = Node(val, self.dummy.next)
        self.dummy.next = newHead
        self.length += 1

        self.printLinkedList()


    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next

        newTail = Node(val)
        current.next = newTail
        self.length += 1

        self.printLinkedList()


    def addAtIndex(self, index: int, val: int) -> None:

        if index>self.length:
            return

        if index==self.length:
            self.addAtTail(val)
            return

        i = 0
        prev = self.dummy

        while i<index:
            prev = prev.next
            i+=1

        currentNode = Node(val)
        nextNode = prev.next
        prev.next = currentNode
        currentNode.next = nextNode

        self.length += 1
        self.printLinkedList()

    def deleteAtIndex(self, index: int) -> None:
        
        i = 0

        if not index<self.length:
            return

        prev = self.dummy

        while i<index:
            prev = prev.next
            i+=1

        prev.next = prev.next.next
        self.length -= 1

        self.printLinkedList()


    def printLinkedList(self):
        # current = self.dummy.next

        # print("LINKEDLIST:")
        # while current:
        #     print(current.val)
        #     current = current.next
        # print("====================")        
        pass

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)