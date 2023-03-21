def monotonicIncreasing(arrOfNumbers):
    stack = []

    for i in arrOfNumbers:
        if stack and stack[-1] >= i:
            stack.pop()
        stack.append(i)
    return stack

print(monotonicIncreasing([5,2,6,3]))