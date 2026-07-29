class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = dict()
        ans = 0
        tmp = list(set(word))
        for c in word:
            dic[c] = dic.get(c, 0) + 1
        tmp.sort(key=lambda x :dic[x],reverse=True)
        for i in range(len(tmp)):
            ans += dic[tmp[i]] * (i // 8 + 1)
        return ans
