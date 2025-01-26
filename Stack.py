class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=Node(data)
        if self.top is None:
            self.top=newnode
        else:
            newnode.Next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            print('Stack is empty..')
        else:
            self.top=self.top.Next
    def print(self):
        temp=self.top
        while temp:
            print(temp.data,end=' ')
            temp=temp.Next
        print()
    def Reverse(self):
        temp=self.top
        while temp:
            r.push(temp.data)
            temp=temp.Next
s=Stack()
r=Stack()
s.push(10)
s.push(20)
s.push(30)
s.print()
# s.pop()
s.print()
s.Reverse()
r.print()
