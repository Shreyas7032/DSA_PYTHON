class BST:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
    def insert_Node(self,newnode):
        if newnode.data<self.data:
            if self.left==None:
                self.left=newnode
            else:
                self.left.insert_Node(newnode)
        else:
            if self.right==None:
                self.right=newnode
            else:
                self.right.insert_Node(newnode)
def inorder_traversal(self):
    if self==None:
        return
    inorder_traversal(self.left)
    print(self.data,' ')
    inorder_traversal(self.right)
def preorder_Traversal(self):
    if self==None:
        return
    print(self.data,end=' ')
    preorder_Traversal(self.left)
    preorder_Traversal(self.right)
def postorder_Traversal(self):
    if self==None:
        return
    print(self.data,end=' ')
    preorder_Traversal(self.left)
    preorder_Traversal(self.right)
    print(self.data,end=' ')
    
def min(self):
    if self.left==None:
        print('Min Value:',self.data)
    else:
        min(self.left)
def max(self):
    if self.right==None:
        print('Max Value:',self.data)
    else:
        max(self.right) 

def delete(self,value):
    if self==None:
        return self
    if value<self.data:
        self.left=delete(self.left,value)
    if value>self.data:
        self.right=delete(self.right,value)
    else:
        if self.left==None:
            return self.right
        if self.right==None:
            return self.left  
def search_Node(self,value):
    if self is None:
        print('Node Not Found..')
        return
    if value==self.data:
        print('Node Found')

    elif value<self.data:
        search_Node(self.left,value)
    else:
        search_Node(self.right,value)
        
        
        
root=BST(10)
root.insert_Node(BST(12))
root.insert_Node(BST(14))
root.insert_Node(BST(11))
print('Inorder...')
inorder_traversal(root)
# print('prorder....')
# preorder_Traversal(root)
# print('postorder...')
# postorder_Traversal(root)
# print('Min Element...')
# min(root)
# max(root)
search_Node(root,12)
