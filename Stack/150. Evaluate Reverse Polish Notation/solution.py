class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+', '-', '*', '/']
        stack = []


        for i in range(len(tokens)):
            if tokens[i] in operators:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(val1 + val2)
                if tokens[i] == '/':
                    stack.append(val1 / val2)
                if tokens[i] == '*':
                    stack.append(val1 * val2)
                if tokens[i] == '-':
                    stack.append(val1 - val2)
                continue
            stack.append(tokens[i])
        return int(stack.pop())