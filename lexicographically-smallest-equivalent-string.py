class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {}
        for i in range(len(s1)):
            rep[s1[i]] = s1[i]
            rep[s2[i]] = s2[i]
            
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)
        
            if x_rep != y_rep:
                if x_rep <= y_rep:
                    rep[y_rep] = rep[x_rep]
                else:
                    rep[x_rep] = rep[y_rep]
        for i in range(len(s1)):
            union(s1[i], s2[i])
        ans = ""
        for i in baseStr:
            if i in rep:
                x = find(i)
                ans += x
            else:
                ans += i
        return ans