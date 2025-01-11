class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
class LL:
    def __init__(self):
        self.head=self.tail=None
    
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.tail=newnode
        else:
            self.tail.Next=newnode
            self.tail=newnode
    def print(self):
        if self.head is None:
            print('LL is empty..')
        else:
            temp=self.head
            while temp:
                print(temp.data,end='==>')
                temp=temp.Next
            print()
    def Even_Odd_Linked_List(self):
        evenList=LL()
        oddList=LL()
        
        temp=self.head
        while temp:
            if temp.data % 2 ==0:
                evenList.insert_end(temp.data)
            else:
                oddList.insert_end(temp.data)
            temp=temp.Next
        return evenList,oddList
        
        
        
l1=LL()
l1.insert_end(12)
l1.insert_end(14)
l1.insert_end(16)
l1.insert_end(11)
l1.insert_end(17)


l1.print()
evenList,oddlist=l1.Even_Odd_Linked_List()
evenList.print()
oddlist.print()
