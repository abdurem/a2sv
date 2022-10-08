class Solution:
    def compress(self, chars: List[str]) -> int:
        letter=chars[0]
        num=0
        ans=[]
        for i in chars:
            if letter == i:
                num+=1
            else:
                ans.append(letter)
                if num not in [1]:
                    tmp=str(num)
                    for t in tmp:
                        ans.append(t)
                letter=i
                num=1
        ans.append(letter)
        if num not in [1]:
            tmp=str(num)
            for t in tmp:
                ans.append(t)
        chars[:] = ans
        return len(ans)
                