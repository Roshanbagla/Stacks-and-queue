"""Creating stacks."""


def create_stack():
    stack = []
    return stack


def isEmpty(stack):
    if len(stack) == 0:
        return True


def push(stack, item):
    stack.append(item)
    print("Pushed to stack " + str(item))


def pop(stack):
    if (isEmpty(stack)):
        return "Stack is empty"
    else:
        stack.pop()
    return stack


stack = create_stack()
print(pop(stack))
push(stack,10)
