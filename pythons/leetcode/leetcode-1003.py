class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == 'c':
                if len(stack) == 0:
                    return False
                if stack[-1] != 'b':
                    return False
                else:
                    stack.pop()
                    if len(stack) == 0:
                        return False
                    if stack[-1] != 'a':
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0