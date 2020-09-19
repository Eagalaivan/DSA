# Journey starts here DSA
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def printNodes(self):
        if self.head==None:
            print("head is null")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp=temp.next
    def countNodes(self):
        if self.head == None:
            print("head is null")
        else:
            temp = self.head
            count=0
            while temp is not None:
                count+=1
                temp=temp.next
            print("count nodes",count)
object= SinglyLinkedList()
node1= Node(1)
object.head=node1
node2= Node(2)
node3= Node(3)
node4= Node(4)
node1.next=node2
node2.next=node3
node3.next=node4
# print(node3.value,node4.value,node2.value,node1.value)
object.printNodes()
object.countNodes()