class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []
        for a in s:
            if a in matches:
                if stack and stack[-1] == matches[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        return True if not stack else False