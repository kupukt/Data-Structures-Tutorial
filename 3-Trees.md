# Trees

Trees are a lot like linked lists except that they can connect to more than just one node. There are different types of trees that are good at doing certain things better than others. 


## Tree Structure

A tree has unique names for each element of the tree. The very top of the tree which is the starting node is called the root or parent. The splitting nodes are called subtrees and this continues until a subtree no longer has anymore nodes to branch out to, this is where it is called the leaf, where the tree ends on that portion of the tree.

Here are some different types of trees

## Binary Tree

A binary tree is a tree where each node can only be connected to two other child nodes.

A diagram of a binary tree:

![Binary Tree](/Pictures/binarytree.png)

## Binary Search Tree

One of the most popular trees are built from a binary tree and that is the binary search tree. A binary search tree is a binary tree that follows a set of rules that are put in place for the data

For example, in this diagram, the binary tree is following a rule of a lesser value than the previous node is on the left of the node and a greater value is on the right.

![Binary Search Tree](/Pictures/binarysearch.png)

These binary trees are used in all different types of ways like finding values at a fast rate to storing data for literal family trees that companies like ancestry use.

Binary search trees ares very efficient and one of the fastest running data structures out there. When you look through a tree to remove, add, or find a value, the big o notation is O(log n) because it is basically splitting the tree in half everytime since you don't have to search the side of the tree that was passed.

To traverse the tree it takes an O(n) time because of the need for recursion.

## Problem Solving

In order to get a good understanding of binary trees, here is a problem to try out:

1. Find the height of a non binary tree only counting the shorter side.

## Solution

Here is a sample solution to the problem:

[Binary Tree Solution](binarytreesolution.py)

### Home

[Back to Homepage](0-Welcome.md)