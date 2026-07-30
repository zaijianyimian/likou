class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0

        # 相邻字符串是否已经确定顺序
        sorted = [False] * (len(strs)-1)

        for j in range(len(strs[0])):  # 列
            delete = False

            for i in range(len(strs)-1):  # 相邻字符串
                if sorted[i]:
                    continue

                if strs[i][j] > strs[i+1][j]:
                    delete = True
                    break

            if delete:
                ans += 1
                continue

            # 当前列保留，更新确定关系
            for i in range(len(strs)-1):
                if strs[i][j] < strs[i+1][j]:
                    sorted[i] = True

        return ans