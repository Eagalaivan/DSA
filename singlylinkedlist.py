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
    def serachNode(self,elem):
        if self==None:
            print("no nodes linkeds head is None")
        else:
            pos=1
            temp=self.head
            while temp is not None:
                if temp.value == elem:
                    print("found at pos",pos)
                pos+=1
                temp = temp.next
    def insertfirst(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
    def insertlast(self,value):
        temp=Node(value)
        if self.head is None:
            self.head = temp
            return
        else:
            p=self.head
            while p.next is not None:
                p=p.next
            p.next=temp
    def insertafternode(self,value):
        p=self.head
        while p is not None:
            if p.value == value:
                break
            p=p.next
            if p is None:
                print(value,"not found")
            else:
                temp=Node(value)
                temp.next=p.next
                p.next=temp
    def insertbeforenode(self,value):
        if self.head is None:
            print("empty list")
            return
        if value == self.head.value:
            temp=Node(value)
            temp.next=self.head
            self.head = temp
            return
        p=self.head
        while p.link is not None:
            if p.next.value == value:
                break
            p=p.next
        if p.next is None:
            print("value","not present in list")
        else:
            temp=Node(value)
            temp.next=p.next
            p.next=temp
    def insertatposition(self,value,pos):
        if pos==1:
            temp=Node(value)
            temp.next=self.head
            self.head=temp
            return
        p=self.head
        i=1
        while i<pos-1 and p is not None:
            p=p.next
            i+=1
        if p is None:
            print("can only inset up postion",i)
        else:
            temp=Node(value)
            temp.next=p.next
            p.next=temp
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
object.serachNode(3)
object.insertfirst(0)
object.insertlast(5)
object.insertafternode(5)
object.printNodes()