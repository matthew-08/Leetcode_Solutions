class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        resut = []

        def backtrack(o, closed):
            if o == closed == n:
                res.append("".join(stack))
                return
            
            if o < n
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if closed < open;
            