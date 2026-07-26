# 394 字符串解码
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        multi = 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = '', 0
            elif c == ']':
                curMulti, lastRes = stack.pop()
                res = lastRes + curMulti * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res
