class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        counts = Counter(s)
        target = n // 4
        left, right, ans = 0, 0, n
        
        while right < n:
            counts[s[right]] -= 1
            while left < n and all(count <= target for count in counts.values()):
                ans = min(ans, right - left + 1)
                counts[s[left]] += 1
                left += 1
            right += 1
        
        return ans