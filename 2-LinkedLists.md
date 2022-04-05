# Linked Lists

What exactly is a linked list? A linked list is another linear data structure just like a stack but have almost nothing in common. Linked lists are more like arrays when it comes to structure and purpose. What makes a linked list different from an array is that it is not in a fixed position. In an array, every piece of information is in a fixed spot with bordering information as well. In order perform actions such as adding or removing from an array, you need to find a spot to put the information in and then the program has to move every other element over and into a new position taking up time. With a linked list, you can simply traverse the list and  create a new node wherever you want without having to reposition every node after or before the new one. 

## Structure of Linked List

The structure of a linked list is simple. In this example, we'll only be going over a singly linked list and a doubly linked list.
A linked list contains `nodes`. A singly linked list node will contain some sort of data, and a next portion, which is the pointer that connects the nodes together.

In this diagram here, we see how linked lists connect to each other.

This first picture is a single linked list. This means that the nodes are only connected one way meaning that the list can only be traversed one way.

![Single Link List](/Pictures/singlelinklist.png)

In a doubly linked list, the node consists of data, a next pointer, and a previous pointer. This type of linked list can be traversed both ways.

![Double Link List](/Pictures/doublelinklist.png)

Now seeing these diagrams of linked lists is cool and all but what does it look like to create this by actually programming? Here is what that would sort of look like:

```python
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
```
This is what would be required to make just the very first node of a linked list. When it comes to the efficiency of linked lists, it is both fast and slow. In order to create or remove the head or tail of a linked list, it is a big o of O(1) because they're both on the end of the list and don't require searching. In order to create or remove a node inbetween the head and tail takes a big o of O(n) because it requires a loop to iterate through the list in order to find the node.

## Problem Solving

Linked Lists are fun to work with but are a bit of a challenge too. Here is a challenge for you:

1. Create a function that will iterate through a linked list and replace any values under a certain amount, or over a certain amount with a new value.


## Solution

Here is a sample solution to the problem above:

[Linked List Solution](linkedlistsolution.py)