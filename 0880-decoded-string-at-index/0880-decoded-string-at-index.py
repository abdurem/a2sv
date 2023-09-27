class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        for char in s:
            if char.isdigit():
                n *= int(char)
            else:
                n += 1

        for char in reversed(s):
            k %= n
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                n /= int(char)
            else:
                n -= 1