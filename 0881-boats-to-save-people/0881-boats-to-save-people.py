class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lft=0
        rgt=len(people)-1
        ans=0

        while lft<=rgt:
            if lft==rgt:
                ans+=1
                break
            elif people[lft]+people[rgt] <= limit:
                ans+=1
                lft+=1
                rgt-=1
            elif people[lft]+people[rgt] > limit:
                ans+=1
                rgt-=1
            
        return ans