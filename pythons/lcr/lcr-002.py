class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            tmpI = int(a[i]) if i >= 0 else 0
            tmpJ = int(b[j]) if j >= 0 else 0

            i -= 1
            j -= 1
            sum = tmpI + tmpJ + carry
            carry = sum / 2
            ans.append(str(sum % 2))
        if carry > 0:
            ans.append(carry)
        return ''.join(reversed(ans))