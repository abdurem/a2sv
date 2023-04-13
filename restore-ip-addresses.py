class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, dots):
            if dots == 0:
                if start == len(s):
                    res.append(".".join(curr))
                return
            
            for end in range(start+1, min(start+4, len(s)+1)):
                segment = s[start:end]
                if len(segment) > 1 and segment[0] == "0":
                    continue
                if int(segment) > 255:
                    continue
                curr.append(segment)
                backtrack(end, dots-1)
                curr.pop()
        
        res = []
        curr = []
        backtrack(0, 4)
        return res