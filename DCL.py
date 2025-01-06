class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.Next=None
        
class DCL:
    def __init__(self):
        self.head=None
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.Next=self.head
            newnode.prev=self.head
        else:
            temp=self.head
            while temp.Next!=self.head:
                temp=temp.Next
            temp.Next=newnode
            newnode.prev=temp
            newnode.Next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.Next=self.head
            newnode.prev=self.head
        else:
            temp=self.head
            while temp.Next!=self.head:
                temp=temp.Next
            temp.Next=newnode
            newnode.prev=temp
            newnode.Next=self.head
            self.head.prev=newnode
    def print(self):
        if self.head is None:
            print('LL is empty..')
        else:
            temp=self.head
            while temp:
                print(temp.data,end='==>')
                temp=temp.Next
                if temp==self.head:
                    break
            print()
    def delete_at_start(self):
        if self.head is None:
            print('LL is empty')
        elif self.head.Next==self.head:
            self.head=None
        else:
            temp=self.head
            while temp.Next!=self.head:
                temp=temp.Next
            temp.Next=self.head.Next
            self.head.Next.prev=temp
            self.head=temp.Next
            
    def delete_at_end(self):
        if self.head is None:
            print('LL is empty')
        elif self.head.Next==self.head:
            self.head=None
        else:
            temp=self.head
            while temp.Next.Next!=self.head:
                temp=temp.Next
            temp.Next=self.head
            self.head.prev=temp
            
        
            
l=DCL()
l.insert_at_start(10)
l.insert_at_start(12)
l.insert_at_start(14)
l.print()
l.insert_at_end(8)
l.insert_at_end(6)
l.insert_at_end(4)
l.print()
l.delete_at_start()
l.print()
l.delete_at_end()
l.print()
            
            
            
            