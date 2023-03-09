class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query = []
        arr = []
        ans = []
        for que in queries:
            query.append(que.count(min(que)))
        for wor in words:
            arr.append(wor.count(min(wor)))
        arr.sort()
        for q in query :
            num = len(words) - bisect.bisect_right(arr,q)
            ans.append(num)
        return ans