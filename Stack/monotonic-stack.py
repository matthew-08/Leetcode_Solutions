# A monotonic stack is a stack which will always be either decreasing or increasing.

# Let's say we have an input array:
# inputArray = [5,7,8,6]
# We're looking for a monotonically increasing stack

# As we push these numbers into a stack, we must stick the principle that this stack can only be increasing
# Stack = [5]

# Stack = [5,7] - so far still increasing - all good.

# Stack = [5,7,8] - Again, still increasing.  8 is greater than the number that preceded it.

# Stack = [5,7,8] <= 6.  Let's pause here.  We need to get 6 onto the stack.  If we push 6 to the stack as is -
# it would break the monotonically increasing structure we're adhering to.  So what do we do?

# Remove the top of stack.

# Stack = [5,7] <= 6  We removed the top of the stack and again, the top of the stack is greater than the number
# we're pushing.  We remove it as well.

# Stack = [5] <= 6.  We can finally push 6.
# The result: Stack = [5,6]

def monotonicIncreasing(arrOfNumbers):
    stack = []

    for i in arrOfNumbers:
        if stack and stack[-1] >= i:
            stack.pop()
        stack.append(i)
    return stack

print(monotonicIncreasing([5,2,6,3]))

def monotonicDecreasing(arrOfNumbers):
    stack = []

    for i in arrOfNumbers:
        if stack and stack[-1] <= i:
            stack.pop()
        stack.append(i)
        return stack
    


input = [3,7,2]