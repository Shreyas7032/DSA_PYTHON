class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class LL:
    def __init__(self):
        self.head = self.tail = None

    def insert_Node_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
        else:
            self.tail.Next = newnode
            self.tail = newnode

    def print(self):
        temp = self.head
        if temp is None:
            print('LL is empty...')
        else:
            while temp:
                print(temp.data, end=' ')
                temp = temp.Next
            print()

    # Merge two linked lists
    def merge(self, other_list):
        if self.head is None: #If the first list is empty
            self.head=other_list.head
            self.tail=other_list.tail
        else:
            self.tail.Next=other_list.head
            self.tail=other_list.tail
            other_list.head=None #update the otherlist head

# Test the merge operation
list1 = LL()
list1.insert_Node_end(1)
list1.insert_Node_end(3)
list1.insert_Node_end(5)

list2 = LL()
list2.insert_Node_end(2)
list2.insert_Node_end(4)
list2.insert_Node_end(6)

print("List 1:")
list1.print()

print("List 2:")
list2.print()

# Merge the two lists
list1.merge(list2)

print("Merged List:")
list1.print()
