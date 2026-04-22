from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtrack(s, 0, 0, "", res)
        return res
    def backtrack(self,s,index,count,path,res):
        if count == 3:
            if self.isValid(s,index,len(s) - 1):
                path = path + s[index:]
                res.append(path)
            return
        for i in range(index,min(index + 3,len(s))):
            if self.isValid(s,index,i):
                self.backtrack(s,i + 1,count + 1,path + s[index:i+1] + ".",res)
            else:
                break
    def isValid(self,s,start,end):
        if start > end:
            return False
        if s[start] == "0"and start != end:
            return False
        num = 0
        for i in range(start,end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True