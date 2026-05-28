class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lo = [0] * 26
        mask = set()
        se = set()
        upseen = set()
        for ch in word:
            if ch.islower():
                lo[ord(ch) - ord('a')] += 1
                up = ch.upper()
                if up in se:
                    se.remove(up)
                    mask.add(up)
            else:
                if ch in upseen:
                    continue
                upseen.add(ch)
                if ch in se:
                    continue
                if lo[ord(ch) - ord('A')] > 0 and ch not in mask:
                    se.add(ch)
        return len(se)
if __name__ == "__main__":
    s = Solution()
    str = "AbcbDBdD"
    print(s.numberOfSpecialChars(str))