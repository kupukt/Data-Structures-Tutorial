class LinkedList:
    
    class Node:
        

        def __init__(self, data):
            
            self.data = data
            self.next = None
            self.prev = None

        def __init__(self):
        
            self.head = None
            self.tail = None

        def insert_head(self, value):
        
            
            new_node = LinkedList.Node(value)  
            
        
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            
            else:
                new_node.next = self.head 
                self.head.prev = new_node 
                self.head = new_node

        def replace(self, old_value, new_value):
               

                curr = self.head
                while curr is not None:
                    if curr.data > old_value or curr.data < old_value :
                        curr.data = new_value
                    curr = curr.next