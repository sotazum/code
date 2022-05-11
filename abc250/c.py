class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next


head = Node(0)
l = LinkedList()
l.head = head
n, q = map(int, input().split())
cur = head
for i in range(1, n+1):
    cur.next = Node(i)
    cur = cur.next

l.printList()