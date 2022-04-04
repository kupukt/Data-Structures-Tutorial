# Stacks

Stacks are just one of the many data structures used in programming today. A stack is a linear data structure
in that it follows one path. This is explained simply in FILO or LOFI. FILO is first in last out, and LOFI
is last out first in. We can think of stacks as literal stacks, stacking up plates, taking out pringles from a pringle can, and
anything else that has to do with

## Operations With Stacks

Stacks have basic functions that are performed with it to allow it to do what it was meant to do and also functions that are there that are practicle for the data structure. Here are the Functions:

* Append
* Pop
* Empty
* Size

### Append

Append is an operation used with a stack to add items to the back of the stack.
Append has a big o notation of O(1), because it runs at O(1), it will always take the same time to execute
For Example:

```python
stack = []
number = 43
stack.append(number)
print(stack)
```

### Pop

Pop is an operation that is used to remove an item from the back of the stack. Pop also has a big o notation of O(1) so everytime it is used, it will always take the same amount of time to perform the action

``` python
stack = []
number = 43
number2 = 56
stack.append(number)
stack.append(number2)
print(stack)
stack.pop()
print(stack)
```

There are many other operations that go with stacks but these are the two main ones to really understand 

# Uses

Stacks are most commonly used to keep track of things in order since you can only add or remove an element from one side of the stack. The biggest implementation when it comes to a stack is the undo shortcut on multiple different platforms. Can you imagine accidentally deleting your whole paper and not being able to get it back? Luckily stacks prevent that from happening. The undo feature is a stack that stores the state  or action that was last inputed into a stack and when you choose to undo with control z, the last action is popped and removed from the stack leaving you with a different state.

# Problem Solve

Now that you know a little bit about stacks, here is a problem to solve that deals with what you have just been taught.

Here are the requirements:

1. Initialize  a stack.
2. Add a string into the stack.
3. Display the string backwards in a separate stack.


## Solution

Here is a sample solution to the problem:
[Stack Solution](stacksolution.py)



