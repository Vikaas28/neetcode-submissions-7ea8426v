class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            k=0
            for pile in piles:
                k+=math.ceil(pile/mid)
            if k<=h :
                ans=mid
                r=mid-1
            else:
                l=mid+1  
        return ans         



