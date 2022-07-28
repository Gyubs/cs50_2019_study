class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # linked list 출력
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    # Head에 node 추가
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

        # NewNode -> first Node, Head 데이터 NewNode로 변경
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Tail에 node 추가
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    # 두 Node 사이에 NewNode 추가
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node -> second node
list.headval.nextval = e2

# Link second Node -> third node
e2.nextval = e3

# Head
list.AtBegining("Sun")
# Tail
list.AtEnd("Fri")
# Between
list.Inbetween(e3,"Thu")

list.listprint()
'''
Sun
Mon
Tue
Wed
Thu
Fri
'''