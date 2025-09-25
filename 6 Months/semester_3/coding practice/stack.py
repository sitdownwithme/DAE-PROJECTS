# stack.py
# -----------------------------------------------------------------------------
# Your task: implement a simple Stack using a Python list.
#
# Functions to implement:
#   1. push(value)    -> put value on top of the stack
#   2. pop()          -> remove and return the top value, or None if empty
#   3. peek()         -> return the top value without removing it, or None if empty
#   4. is_empty()     -> return True if the stack has no items
#   5. size()         -> return how many items are in the stack
# -----------------------------------------------------------------------------

# The stack should be stored in a list called "stack"
stack = []

def push(pancakes):
    # TODO: add value to the top of the stack
    # Write your code here
    stack.append(pancakes)
        


def pop():
    # TODO: remove and return the top value, or None if empty
    # Write your code here
    if len(stack) == 0:
        return None
    else: 
        return stack.pop()

     
def peek():
    # TODO: return the top value without removing it, or None if empty
    # Write your code here
     if len(stack)==0:
         return None
     else:
        return stack[-1]

          
def is_empty():
    # TODO: return True if stack is empty, else False
    # Write your code here
    if len(stack)==0:
        return True
    else:
        return False 
     
def size():
    # TODO: return how many items are in the stack
    # Write your code here
    return len(stack)



stack.clear()
push("strawberry") 
print(stack)
push("grape")
print(stack)
push("blueberry")
push("chocolatechip")
push("cinnamon")
print(stack)
pop()
print(stack)
print(peek)
print(is_empty())
print(size())
push(stack)
push("cinnamon")
print (stack) 
pop()
print(stack)
print(peek)
pop()
pop()
pop()
print(stack)
print(size())
print(peek)
push("mixedberries")
print(stack)
push("apple")
push("orange")
push("yellow")
push("purple")
push("pink")
push("green")
print(stack)
pop()
pop()
pop()
print(stack)
print(size()) 