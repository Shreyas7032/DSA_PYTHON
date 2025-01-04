class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None
        
class LL:
    def __init__(self):
        self.head=self.tail=None
    def insert_Node_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.tail=newnode
        else:
            self.tail.Next=newnode
            self.tail=newnode
    def insert_Node_front(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.tail=newnode
        else:
            newnode.Next=self.head
            self.head=newnode
    def delete_At_Start(self):
        if self.head is None:
            print('LL is Empty..')
        else:
            self.head=self.head.Next
    def delete_at_end(self):
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp!=self.tail:
                temp=temp.Next
            temp.next=None
            self.tail=temp
    def count_Nodes(self):
        temp=self.head
        count=0
        while temp:
            temp=temp.Next
            count=count+1
        print("The No Of Nodes In Linked List Are:",count)
        
    def max_Node(self):
        if self.head==None:
            print('LL is empty..')
        else:
            temp=self.head
            maxvalue=temp.data
            while temp:
                if temp.data>maxvalue:
                    maxvalue=temp.data
                temp=temp.Next
            print('Max Value is:',maxvalue)
    def min_Node(self):
        temp=self.head
        minvalue=temp.data
        while temp:
            if(temp.data<minvalue):
                minvalue=temp.data
            temp=temp.Next
        print('Min Value Is:',minvalue)
        
        
        
    def print(self):
        temp=self.head
        if temp is None:
            print('LL is empty...')
        else:
            while temp:
                print(temp.data,end=' ')
                temp=temp.Next
    
l=LL()
l.insert_Node_end(10)
l.insert_Node_end(12)
l.insert_Node_end(13)
l.print()   
l.insert_Node_front(14)
print()
l.print()
l.delete_At_Start() 
print()
l.print()
l.delete_at_end()
print()
l.print()
l.count_Nodes()
l.max_Node()
l.min_Node()
    
            
            
        