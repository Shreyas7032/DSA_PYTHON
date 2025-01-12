class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None  # Next node in the list
        self.Prev = None  # Previous node in the list

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the doubly linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.Next:
                temp = temp.Next
            temp.Next = new_node
            new_node.Prev = temp

    # Delete nodes with negative values
    def delete_negative_values(self):
        temp=self.head
        while temp:
            if temp.data<0:
                if temp==self.head:
                    if self.head.Next:
                        self.head=self.head.Next
                        self.head.prev=None
                    else:
                        self.head=None
                else:
                    if temp.Prev:
                        temp.Prev.Next=temp.Next
                    if temp.Next:
                        temp.Next.Prev=temp.Prev
                temp=temp.Next
            else:
                temp=temp.Next
                    
                

    # Print the doubly linked list
    def print(self):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        while temp:
            print(f"{temp.data}", end=" <=> ")
            temp = temp.Next
        print()

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(-5)
dll.insert_at_end(20)
dll.insert_at_end(-15)
dll.insert_at_end(30)
dll.insert_at_end(-1)

print("Original list:")
dll.print()

dll.delete_negative_values()

print("After deleting negative values:")
dll.print()
