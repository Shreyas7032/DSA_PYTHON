class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
        
class SCL:
    def __init__(self):
        self.head=None
    def insert_at_start(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            newnode.Next=self.head
        else:
            temp=self.head
            while temp.Next!=self.head:
                temp=temp.Next
            temp.Next=newnode
            newnode.Next=self.head
            self.head=newnode
    
    def print(self):
        if self.head is None:
            print('LL is Empty..')
        else:
            temp=self.head
            while True:
                print(temp.data,end='==>')
                temp=temp.Next
                if temp==self.head:
                    break
        print()
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            newnode.Next=self.head
        else:
            temp=self.head
            while temp.Next!=self.head:
                temp=temp.Next
            temp.Next=newnode
            newnode.Next=self.head 
    def delete_at_start(self):
        if self.head is None:
            print('LL is empty..')
        elif self.head.Next==self.head:
            self.head=None
        else:
            temp=self.head
            while temp.Next!=self.head:
                temp=temp.Next
            temp.Next=self.head.Next
            self.head=self.head.Next  
    def delete_at_end(self):
        if self.head.Next==self.head:
            self.head=None
        else:
            temp=self.head
            while temp.Next.Next!=self.head:
                temp=temp.Next
            temp.Next=self.head
        
            
                   
                
l=SCL()
l.insert_at_start(10)
l.insert_at_start(12)
l.insert_at_start(16)
l.insert_at_start(17)
l.print()
l.insert_at_end(8)
l.insert_at_end(6)
l.print()
# l.delete_at_start()
# l.print()
l.delete_at_end()
l.print()
            