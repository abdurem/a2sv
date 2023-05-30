class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dic = {i : i for i in range(len(s))}
        
        def find(val):
            if dic[val] != val:
                dic[val] = find(dic[val])
            return dic[val]
        
        def union(a,b):
            ap = find(a)
            bp = find(b)
            sm = (min(a,b))
            dic[ap] = dic[bp] = dic[a] = dic[b] = sm
        
        for a,b in pairs:
            union(a,b)
        
        parents = defaultdict(list)
        for i in dic:
            temp = find(i)
            parents[temp].append((s[i],i))

        for i in parents:
            parents[i].sort(reverse=True)
        
        result = []

        for i in range(len(s)):
            p = find(i)
            result.append(parents[p].pop()[0])

        return ("".join(result))