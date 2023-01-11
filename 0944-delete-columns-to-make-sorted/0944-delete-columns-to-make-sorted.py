class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0

        for i in range(len(strs[0])):
            tmp=[]
            for j in range(len(strs)):
                tmp.append(strs[j][i])
            if tmp != sorted(tmp):
                ans+=1
        return ans