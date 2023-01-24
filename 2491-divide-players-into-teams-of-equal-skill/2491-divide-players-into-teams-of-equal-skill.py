class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2 == 1:
            return -1
        
        skill.sort()
        ans=0
        l=0
        r=len(skill)-1
        tmp=skill[l]+skill[r]
        while l < r:
            if skill[l]+skill[r] != tmp:
                return -1
            ans+= (skill[l]*skill[r])
            l+=1
            r-=1
        return ans