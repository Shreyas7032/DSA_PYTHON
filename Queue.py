class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
class Q:
    def __init__(self):
        self.front=self.rear=None
    def enque(self,data):
        newnode=Node(data)
        if self.front is None:
            self.front=self.rear=newnode
        else:
            self.rear.Next=newnode
            self.rear=newnode
    def print(self):
        temp=self.front
        if temp is None:
            print('Q is empty')
        while temp: 
            print(temp.data,end='==>')
            temp=temp.Next
        print()
q=Q()
q.enque(10)
q.print()
q.enque(20)
q.print()

