class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x:len(x))
        pre=strs[0]
        for i in range(len(pre),0,-1):
            if all([pre[:i]==strs[j][:i] for j in range(1,len(strs))]):
                return pre[:i]
        return ''