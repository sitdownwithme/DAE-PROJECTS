stack = ["i love you" ]
def push(value):
    stack.append(value)
push("i want you ")
push("i care about you ")
print(stack)
push("i need you")
push("be kind")
push("be gentle")
push("be good")
push("love is in the air")
print(stack)

def pop():
    if len(stack)==0:
        return None
    else:
        return stack.pop() 


print(pop())
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)
