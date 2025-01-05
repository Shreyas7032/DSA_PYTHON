class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Doubly_Linear:
    def __init__(self):
        self.head = self.tail = None

    def insert_Node_Start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_Node_End(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None

    def delete_start(self):
        if self.head is None:
            print('LL is empty; cannot delete')
        elif self.head==self.tail:
            self.head=None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print('LL is empty; cannot delete')
        elif self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" ==> " )
            temp = temp.prev
        print()  

    def print(self):
        if self.head is None:
            print('LL is Empty..')
        else:
            temp = self.head
            while temp:
                print(temp.data, end=' ==> ')
                temp = temp.next
            print()

# Testing the code
l1 = Doubly_Linear()
l1.insert_Node_Start(10)
l1.insert_Node_Start(12)
l1.insert_Node_Start(14)
# l1.print() 

# l1.insert_Node_End(8)
# l1.insert_Node_End(6)
l1.print() 

l1.delete_start()
l1.print()

# l1.delete_end()
# l1.print() 

# l1.reverse()  # Expected: 8 ==> 10 ==> 12 ==>
